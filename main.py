from fastapi import FastAPI
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can specify specific origins if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define the GET method that returns "Hello world" as JSON
@app.get("/")
def read_root():
    return {"message": "Hello world"}

# Define the POST method that takes a JSON, counts the number of keys, and returns the count
@app.post("/parse_email/")
def count_keys(json_data: Dict):
    num_keys = len(json_data.keys())
    print(json_data)
    return {"number_of_keys": num_keys}

# Run the FastAPI server using Uvicorn (if running as a script)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
