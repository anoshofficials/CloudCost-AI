from fastapi import FastAPI

app = FastAPI(
    title="CloudCost AI"
)

@app.get("/")
def root():
    return {
        "message": "CloudCost AI is running!"
    }
