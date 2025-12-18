import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings



load_dotenv()

pinecone_api = os.getenv("PINECONE_API_KEY")
openai_embedding_small_api = os.getenv("OPENAI_API_KEY_EMBEDDING")


index_name = "yt-embeddings2"  # change if desired

pc = Pinecone(api_key=pinecone_api)

endpoint = "https://models.github.ai/inference"
model_name = "openai/text-embedding-3-small"

embeddings = OpenAIEmbeddings(
    model=model_name,
    base_url=endpoint,
    api_key=openai_embedding_small_api
)

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

index = pc.Index(index_name)

vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

def similarity_search(user_query : str , k = 3) -> list: 
    
    #vector similarity search format : [Document(id='01372e0f-4f5a-47bc-b195-ff39ca19ea86', metadata={}, page_content="real and subscribe to the Space Race for more videos just like this we do one long form essay and one news update every week and if you'd like more we've got two more on the screen for you right now"),
 
    results = vector_store.similarity_search(
        user_query,
        k =k
    )
    # can covert this list into string context too, TO-DO
    return results

def get_retriever():
 
    retriever = vector_store.as_retriever()
    
    return retriever

def get_context(user_query :str) -> str:
    
    retriever = vector_store.as_retriever()
    retrieved_docs = retriever.invoke(user_query)
    
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)
    
    return context

