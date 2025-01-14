from fastapi import FastAPI
from app.api.analyze import router as test_router

app = FastAPI()

# Include the test router with prefix `/test`
app.include_router(test_router, prefix="/test")

# Placeholder for OpenAI-related functionality
@app.get("/openai")
def openai_functionality():
    return {"message": "OpenAI integration will be here!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
