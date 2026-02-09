# from fastapi import FastAPI
import smtplib
from email.message import EmailMessage
import ssl
import smtplib
from fastapi.middleware.cors import CORSMiddleware



sender="suryaprakash04112001@gmail.com"
recvier="maharagul2002@gmail.com"
pass_word="hove vzwm mkws oeep"

subject="HI This Maha"
body="Hi bro,how are you,enna panndra"

em=EmailMessage()
em['From']=sender
em['To']=recvier
em['Subject']=subject

em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smpt:
    smpt.login(sender,pass_word)
    smpt.send_message(em)
    
print("Mail Sent Successfully ")