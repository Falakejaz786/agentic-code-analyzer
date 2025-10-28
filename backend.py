from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from main import analyze_code_agent  # Your main agentic function

# Initialize FastAPI
app = FastAPI(title="Agentic Code Analyzer API")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace '*' with your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for POST request body
class CodeRequest(BaseModel):
    code: str

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Agentic Code Analyzer API", "status": "running", "endpoints": {"/analyze": "POST - Analyze Python code"}}

# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "healthy"}

# Endpoint to analyze Python code
@app.post("/analyze")
async def analyze_code(request: CodeRequest):
    code = request.code
    if not code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")
    
    try:
        result = analyze_code_agent(code)  # Call main agentic workflow
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional: Run with uvicorn directly
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend:app", host="0.0.0.0", port=port)
