

def making_para(list_of_transcript : list) -> str :
    """
    this function extract text from list of dictionary received from youtube api
    """
    ans_para = ""
    
    for element in list_of_transcript:
        ans_para = ans_para + " " + element['text']
    
    return ans_para