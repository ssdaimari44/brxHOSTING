from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transliterator import Transliterator

# Create FastAPI app
app = FastAPI()

# Allow React frontend (CORS settings)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your React domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize transliterator
model = Transliterator()

# Request model
class TextRequest(BaseModel):
    text: str

# Endpoint
@app.post("/transliterate")
def transliterate_text(req: TextRequest):
    devanagari = model.transliterate(req.text)
    return {"roman": req.text, "devanagari": devanagari}
