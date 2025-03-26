from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from agent import analyze_stock
import uvicorn

app = FastAPI(
    title="Stock Market AI Agent",
    description="An AI-powered agent that analyzes stocks and provides recommendations",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {
        "message": "Stock Market AI Agent is running!",
        "endpoints": {
            "analyze": "/analyze/{ticker}",
            "docs": "/docs"
        }
    }

@app.get("/analyze/{ticker}")
async def analyze(ticker: str):
    """
    Analyze a stock and provide recommendations
    """
    try:
        result = analyze_stock(ticker.upper())
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 