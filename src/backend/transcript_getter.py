# import os, sys
# sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from youtube_transcript_api import YouTubeTranscriptApi
from src.utill.make_para import making_para
# from langchain_core.tools import tool

# @tool
def transcript_eng(video_id: str) -> str : 
    """
    This function accept video id as an argument,  call the youtube transcript api and then return the youtube transcript in english 
    """
    ytt_api = YouTubeTranscriptApi()
    
    fetched_transcript = ytt_api.fetch(video_id)
    
    list_of_dict = fetched_transcript.to_raw_data()
    
    return making_para(list_of_dict)


# if __name__=="__main__":
#     paragraph = transcript_eng("GxyjWhz5VT0")
#     print(paragraph)