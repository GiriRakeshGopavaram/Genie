from fastapi import FastAPI
from pydantic import BaseModel
from backend.app.codegen_model import generate_code
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"] for more secure dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 100
    temperature: float = 0.7

class GenerateResponse(BaseModel):
    result: str

@app.post("/generate", response_model=GenerateResponse)
def generate(prompt_request: PromptRequest):
    result = generate_code(
        prompt=prompt_request.prompt,
        max_tokens=prompt_request.max_tokens,
        temperature=prompt_request.temperature
    )
    return {"result": result}
