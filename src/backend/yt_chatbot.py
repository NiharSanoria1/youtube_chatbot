import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from src.backend.similarity_search import get_context
from src.backend.langchain_pinecone import saving_vector

load_dotenv()

openai_api = os.getenv('OPENAI_API_KEY')

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

llm = ChatOpenAI(
    base_url=endpoint,
    model=model,
    api_key=openai_api
)

def generating_embedding(url :str) : 
    saving_vector(url=url)

def get_ans(url : str , user_query : str ) -> str :
    
    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question} 
        """,
        input_variables=['context', 'question']
    )
    
    context = get_context(user_query=user_query)
    
    final_prompt = prompt.invoke({'context': context, 'question': user_query})
    
    answer = llm.invoke(final_prompt)
    
    return answer