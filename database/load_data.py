import json
import os

from dotenv import load_dotenv
from neo4j import GraphDatabase
from pathlib import Path

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
load_dotenv()
password = os.getenv("NEO4J_PASSWORD", None)
assert password

driver = GraphDatabase.driver(uri, auth=(username, password))

def load_data(data):
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")  # Clear existing data
        for item in data:
            session.run("""
                MERGE (n:Node {name: $name, description: $description})
                """, name=item["name"], description=item["description"])
            if item["parent"]:
                session.run("""
                    MATCH (n:Node {name: $name})
                    MATCH (p:Node {name: $parent})
                    MERGE (p)-[:PARENT_OF]->(n)
                    """, name=item["name"], parent=item["parent"])

def load_json_to_neo4j(json_data):
    def create_node(tx, node):
        query = """
        MERGE (n:Node {name: $name, description: $description})
        RETURN n
        """
        tx.run(query, name=node["name"], description=node["description"])

    def create_relationship(tx, parent_name, child_name):
        query = """
        MATCH (a:Node {name: $parent_name}), (b:Node {name: $child_name})
        MERGE (a)-[:HAS_CHILD]->(b)
        """
        tx.run(query, parent_name=parent_name, child_name=child_name)

    with driver.session() as session:
        for node in json_data["data"]:
            session.write_transaction(create_node, node)
            if node["parent"]:
                session.write_transaction(create_relationship, node["parent"], node["name"])

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
   
    with open(Path(dir_path) / "data.json", "r") as file:
        json_data = json.load(file)
    # load_json_to_neo4j(json_data)
    load_data(json_data.get("data", None))