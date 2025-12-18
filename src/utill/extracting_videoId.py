#Get youtube id
from pytube import extract

def video_id_extractor(url:str) -> str:
   
    id=extract.video_id(url)
    return id

if __name__=="main":
    print(video_id_extractor(""))
