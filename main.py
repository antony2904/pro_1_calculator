from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Calculation(BaseModel):
    x: float
    y: float
    operator: str

@app.post("/calculate")
def calculate(request: Calculation) -> dict[str, float]:
    if request.operator == "+":
        result = request.x + request.y
    elif request.operator == "-":
        result = request.x - request.y
    elif request.operator == "*":
        result = request.x * request.y
    elif request.operator == "/":
        if request.y == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = request.x / request.y
    else:
        raise HTTPException(status_code=400, detail="Unsupported operator")

    return {"result": result}