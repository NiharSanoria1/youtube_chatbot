import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.backend.transcript_getter import transcript_eng
from src.utill.extracting_videoId import video_id_extractor
from pinecone import Pinecone, ServerlessSpec


load_dotenv()

pinecone_api = os.getenv("PINECONE_API_KEY")
openai_embedding_small_api = os.getenv("OPENAI_API_KEY_EMBEDDING")

endpoint = "https://models.github.ai/inference"
model_name = "openai/text-embedding-3-small"

embeddings = OpenAIEmbeddings(
    model=model_name,
    base_url=endpoint,
    api_key=openai_embedding_small_api
)
pc = Pinecone(api_key=pinecone_api)

index_name ="yt-embeddings2"  # change if desired

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

index = pc.Index(index_name)

index_name = "yt-embeddings2"
vector_store = PineconeVectorStore(index=index, embedding=embeddings)

def clean_transcript(text: str) -> str:
    stop_phrases = [
        "subscribe",
        "thumbs up",
        "like the video",
        "two more on the screen",
        "thanks for watching"
    ]
    for phrase in stop_phrases:
        text = text.replace(phrase, "")
    return text


def saving_vector(url : str) :
    video_id = video_id_extractor(url=url)
    paragraph = transcript_eng(video_id=video_id)
    paragraph = clean_transcript(paragraph)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    #return list of text
    texts = text_splitter.split_text(paragraph)

    vector_store_from_texts = PineconeVectorStore.from_texts(
        texts,
        index_name=index_name,
        embedding=embeddings
    )
    
    
def deleting_all_vectors(index_name :str):
    
    index = pc.Index(index_name)
    
    index.delete(delete_all=True)