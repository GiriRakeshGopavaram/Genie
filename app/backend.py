from fastapi import FastAPI
from pydantic import BaseModel
from app.codegen_model import generate_code

app = FastAPI()

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
