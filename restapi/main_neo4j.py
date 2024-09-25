import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from neo4j import GraphDatabase

app = FastAPI()

# Allow CORS for all origins (for simplicity)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
load_dotenv()
password = os.getenv("NEO4J_PASSWORD", None)
assert password

driver = GraphDatabase.driver(uri, auth=(username, password))

class TreeNode(BaseModel):
    name: str
    description: str
    parent: str

def fetch_tree_data():
    with driver.session() as session:
        result = session.run("""
            MATCH (n)
            OPTIONAL MATCH (n)<-[:PARENT_OF]-(parent)
            RETURN n.name AS name, n.description AS description, parent.name AS parent_name
        """)
        nodes = []
        for record in result:
            nodes.append({
                "name": record["name"],
                "description": record["description"],
                "parent": record["parent_name"] if record["parent_name"] else ""
            })
        return nodes

@app.get("/tree", response_model=list[TreeNode])
def get_tree():
    tree_data = fetch_tree_data()
    return tree_data

@app.get("/")
def get_index():
    return "service alive"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_neo4j:app", log_level="info", reload=False, workers=1, port=8000)