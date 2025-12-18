from pinecone import Pinecone, ServerlessSpec
from src.backend.embedding import embedder
from dotenv import load_dotenv
import os

load_dotenv()

pinecone_api = os.getenv('PINECONE_API_KEY')



pc = Pinecone(api_key=pinecone_api)

def saving_embeddings(video_id :str) :
    
    # getting a the list of embedding and list of chunks
    list_of_embedder_result = embedder(video_id=video_id)
    
    list_of_embedding = list_of_embedder_result[0]
    embeddings = [e.embedding for e in list_of_embedding]

    
    list_of_chunks = list_of_embedder_result[1]
    
    index_name = "youtube-embeddings"
    
    #creating pinecone index
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric='cosine',
            spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
            )
        )
    
    vectors = [
        {
            "id":f"vec_{i}",
            "values":embeddings[i],
            "metadata":{
                "text" : list_of_chunks[i]
            }
        }
        for i in range(len(embeddings))
    ]
    
    index = pc.Index(index_name)
    
    batch_upsert(index=index , vectors=vectors)
    
    
def batch_upsert(index, vectors, batch_size=100):
    for i in range(0, len(vectors), batch_size):
        index.upsert(vectors=vectors[i:i+batch_size])
    
    

    
        