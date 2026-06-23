from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/generate")
def generate_voice(input: TextInput):
    # Ici tu brancheras ton vrai modèle Voicebox
    return {"status": "ok", "message": f"Voix générée pour: {input.text}"}
