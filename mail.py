from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models import love
import urllib.parse
import os
import resend

# Resend API Key
resend.api_key = os.getenv("RESEND_API_KEY")

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send-mail")
def send_mail(data: love):
    receiver = data.receiver
    message = data.message

    encoded_message = urllib.parse.quote(message)
    BASE_URL = "https://valentine-mail-app.onrender.com"
    link = f"{BASE_URL}/love?from_mail=Secret%20Admirer&message={encoded_message}"

    resend.Emails.send({
        "from": "Valentine 💖 <onboarding@resend.dev>",
        "to": receiver,
        "subject": "Someone sent you a Valentine 💌",
        "html": f"""
            <h2>{message}</h2>
            <p>Click below to open your Valentine surprise 💖</p>
            <a href="{link}">Open Love Message</a>
        """
    })

    return {"message": "Mail sent successfully 💌"}


@app.get("/love", response_class=HTMLResponse)
def love_page(from_mail: str, message: str = ""):
    return f"""
    <html>
    <head>
    <title>💖 Valentine Message 💖</title>
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        body {{
            margin: 0;
            height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(-45deg, #ff9a9e, #ff6a88, #ff99ac, #fad0c4);
            background-size: 400% 400%;
            animation: gradientBG 12s ease infinite;
        }}

        @keyframes gradientBG {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        .card {{
            position: relative;
            background: rgba(255,255,255,0.95);
            border-radius: 30px;
            padding: 50px 40px;
            max-width: 550px;
            text-align: center;
            box-shadow: 0 20px 50px rgba(255, 0, 102, 0.3);
            animation: floatCard 4s ease-in-out infinite;
        }}

        @keyframes floatCard {{
            0%,100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
        }}

        .title {{
            font-family: 'Great Vibes', cursive;
            font-size: 54px;
            color: #ff2e63;
            margin-bottom: 10px;
            text-shadow: 0 0 15px rgba(255,46,99,0.4);
        }}

        .message {{
            font-size: 20px;
            margin: 25px 0;
            color: #444;
        }}

        .from {{
            font-size: 16px;
            margin-bottom: 25px;
            color: #888;
            font-style: italic;
        }}

        button {{
            padding: 15px 35px;
            font-size: 20px;
            margin: 15px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }}

        .yes {{
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            color: white;
            box-shadow: 0 10px 25px rgba(255, 65, 108, 0.5);
        }}

        .yes:hover {{
            transform: scale(1.1);
        }}

        .no {{
            background: #333;
            color: white;
        }}

        .no:hover {{
            transform: scale(1.05);
        }}

        /* Floating hearts */
        .heart {{
            position: absolute;
            bottom: -20px;
            color: rgba(255, 0, 102, 0.4);
            font-size: 24px;
            animation: floatHearts 8s linear infinite;
        }}

        @keyframes floatHearts {{
            0% {{ transform: translateY(0) scale(1); opacity: 1; }}
            100% {{ transform: translateY(-100vh) scale(1.5); opacity: 0; }}
        }}
    </style>
    </head>

    <body>
        <div class="card">
            <div class="title">Will you be my Valentine? 💖</div>
            <p class="message">{message}</p>
            <div class="from">From: {from_mail}</div>

            <button class="yes" onclick="celebrateLove()">Yes 🌹</button>
            <button class="no" onclick="alert('Oh nooo 💔 But I’ll keep trying 😌')">No</button>
        </div>

        <script>
            function celebrateLove() {{
                alert("YAYYY SHE SAID YES 😍💖");
                for (let i = 0; i < 25; i++) {{
                    let heart = document.createElement("div");
                    heart.className = "heart";
                    heart.style.left = Math.random() * 100 + "vw";
                    heart.style.fontSize = (Math.random() * 20 + 20) + "px";
                    heart.innerHTML = "💖";
                    document.body.appendChild(heart);
                    setTimeout(() => heart.remove(), 8000);
                }}
            }}
        </script>
    </body>
    </html>
    """



# # Start ngrok in a separate thread
# public_url = ngrok.connect(8006)
# print("Your public URL:", public_url)

# # Start FastAPI
# uvicorn.run("main:app", host="0.0.0.0", port=8006, reload=True)