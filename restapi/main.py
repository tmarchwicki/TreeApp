from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins (for simplicity)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = {
  "data": [
    {
      "name": "A",
      "description": "This is a description of A",
      "parent": ""
    },
    {
      "name": "B",
      "description": "This is a description of B",
      "parent": "A"
    },
    {
      "name": "C",
      "description": "This is a description of C",
      "parent": "A"
    },
    {
      "name": "D",
      "description": "This is a description of D",
      "parent": "A"
    },
    {
      "name": "B-1",
      "description": "This is a description of B-1",
      "parent": "B"
    },
    {
      "name": "B-2",
      "description": "This is a description of B-2",
      "parent": "B"
    },
    {
      "name": "B-3",
      "description": "This is a description of B-3",
      "parent": "B"
    }
  ]
}

@app.get("/tree")
def get_tree():
    return data