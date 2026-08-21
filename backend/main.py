from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from auth import LoginRequest, authenticate_user

app = FastAPI(
    title="NovaDev API",
    description="Backend API for NovaDev professional website",
    version="1.0.0"
)

@app.post("/login")
def login(data: LoginRequest):

    if authenticate_user(data.email, data.password):

        return {
            "success": True,
            "message": "Login successful!"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid email or password"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class ContactMessage(BaseModel):
    name: str
    email: str
    message: str


@app.get("/")
def home():
    return {
        "message": "NovaDev API is running"
    }


@app.get("/api/status")
def status():
    return {
        "status": "online"
    }


@app.post("/contact")
def contact(data: ContactMessage):
    print("New contact message:")
    print("Name:", data.name)
    print("Email:", data.email)
    print("Message:", data.message)

    return {
        "success": True,
        "message": "Your message was received successfully!"
    }