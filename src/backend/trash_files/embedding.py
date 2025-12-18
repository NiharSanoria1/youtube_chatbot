import os
from dotenv import load_dotenv
from src.backend.transcript_getter import transcript_eng
from src.backend.chunker import recur_text_splitter
from openai import OpenAI


load_dotenv()
openai_embedding_small_key = os.getenv('OPENAI_API_KEY_EMBEDDING')

endpoint = "https://models.github.ai/inference"
model_name = "openai/text-embedding-3-small"

client = OpenAI(
    base_url=endpoint,
    api_key=openai_embedding_small_key,
)

# video_id = 'GxyjWhz5VT0'

def embedder(video_id : str) -> list:

    """
    this function takes video id and return a list of embedding 
    """
    transcript = transcript_eng(video_id)

    list_of_chunks = recur_text_splitter(transcript)
    
    # this gives us CreateEmbeddingResponse object 
    #ebedding.data have list of embedding to access which we have to do embedding.data[0].embedding which give us the embedding of the first embedding member of list
    embeddings = client.embeddings.create(
        input=list_of_chunks,
        model=model_name
    )
    
    return [embeddings.data, list_of_chunks]
    
    


