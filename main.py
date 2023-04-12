# from flask import Flask, jsonify, request
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello_world():
    return JSONResponse(content={"message": "Hello, World!"})

@app.post("/get_email/")
async def get_email(data: dict):
    print(data)
    return JSONResponse(
        content={"message": "Hello, World!"}
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
