# test_app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SimpleInput(BaseModel):
    name: str
    age: int

@app.post("/test/")
async def test_endpoint(data: SimpleInput):
    return {"message": f"Hello, {data.name}! You are {data.age} years old."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)