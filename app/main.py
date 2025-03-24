from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model.model import summarise_text

# Initialize FastAPI app
app = FastAPI(title="Text Summarisation API")

# Request body schema
class SummarisationRequest(BaseModel):
    text: str
    max_length: int = 150
    min_length: int = 50

@app.get("/")
def root():
    return {"message": "Welcome to the Text Summarisation API. Go to /docs for Swagger UI."}

@app.post("/summarise/")
async def summarise(request: SummarisationRequest):
    try:
        summary = summarise_text(request.text, request.max_length, request.min_length)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in summarising text: {str(e)}")


# Main entry point for the FastAPI app (required to run the app)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)