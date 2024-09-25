import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tree_endpoint():
    response = client.get("/tree")
    assert response.status_code == 200
    data = response.json()
    data_list = data.get("data", None)
    
    # Check that the response is a list
    assert isinstance(data_list, list)
    
    # Check the structure of the json
    
    # Check the structure of the root node
    root_node = next((child for child in data.get("data", None) if child["name"] == "A"), None)
    assert "name" in root_node
    assert "description" in root_node
    assert "parent" in root_node
    assert root_node["parent"] is ""

    # Check the structure of the first child node
    child1 = next((child for child in data.get("data", None) if child["name"] == "B"), None)
    assert child1 is not None
    assert "name" in child1
    assert "description" in child1
    assert "parent" in child1
    assert child1["parent"] is root_node["name"]

    # Check the structure of the second child node
    child2 = next((child for child in data.get('data', None) if child["name"] == "C"), None)
    assert child2 is not None
    assert "name" in child2
    assert "description" in child2
    assert "parent" in child2
    assert child2["parent"] is root_node["name"]

    # Check the structure of the third child node
    child3 = next((child for child in data.get("data", None) if child["name"] == "D"), None)
    assert child3 is not None
    assert "name" in child3
    assert "description" in child3
    assert "parent" in child3
    assert child3["parent"] is root_node["name"]

    # Check the structure of the grandchild nodes
    grandchild1 = next((child for child in data.get("data", None) if child["name"] == "B-1"), None)
    assert grandchild1 is not None
    assert "name" in grandchild1
    assert "description" in grandchild1
    assert "parent" in grandchild1
    assert grandchild1["parent"] is child1["name"]

    grandchild2 = next((child for child in data.get("data", None) if child["name"] == "B-2"), None)
    assert grandchild2 is not None
    assert "name" in grandchild2
    assert "description" in grandchild2
    assert "parent" in grandchild2
    assert grandchild1["parent"] is child1["name"]

    grandchild3 = next((child for child in data.get("data", None) if child["name"] == "B-3"), None)
    assert grandchild3 is not None
    assert "name" in grandchild3
    assert "description" in grandchild3
    assert "parent" in grandchild3
    assert grandchild1["parent"] is child1["name"]
