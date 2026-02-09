from pydantic import BaseModel

class love(BaseModel):
    receiver:str
    message:str
    send_mail:str="valentinesdayspecialbot@gmail.com"
    sender_pass:str= "ogrisjgxsnsgxuou"
    