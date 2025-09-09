from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transliterator import Transliterator

# Create FastAPI app
app = FastAPI()

# Allow frontend (CORS settings)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your Firebase domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize transliterator
model = Transliterator()

# Request model
class TextRequest(BaseModel):
    text: str

# Health check
@app.get("/")
def root():
    return {"message": "Backend is running!"}

# Transliteration endpoint
@app.post("/transliterate")
def transliterate_text(req: TextRequest):
    devanagari = model.transliterate(req.text)
    return {"roman": req.text, "devanagari": devanagari}