from langchain_text_splitters import RecursiveCharacterTextSplitter



def recur_text_splitter(paragraph : str) -> list:
    """
    this function takes transcript paragraph as text and then return a list of chunk of string after recurssive text splitting 
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,  chunk_overlap=10)
        texts = text_splitter.split_text(paragraph)

        return texts
    except Exception as e :
        print("Some error occured with this exception :", e)
    