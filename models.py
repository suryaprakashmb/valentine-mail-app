from pydantic import BaseModel, EmailStr

class love(BaseModel):
    receiver: EmailStr
    message: str
