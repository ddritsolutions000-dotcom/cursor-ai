# FastAPI Integration with AI Code Generator
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_code_generator import AICodeGenerator

app = FastAPI()
ai_generator = AICodeGenerator()

class CodeRequest(BaseModel):
    prompt: str

@app.post("/generate-code")
def generate_code(request: CodeRequest):
    try:
        code = ai_generator.generate_code(request.prompt)
        return {"generated_code": code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating code: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "Cursor AI Backend is Live!"}