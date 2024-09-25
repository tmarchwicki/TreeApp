import React, { useState, useEffect } from "react";
import Tree from "./Tree";
import "./App.css";

const apiUrl = process.env.REACT_APP_API_URL;

function App() {
  const [treeData, setData] = useState([]);
  const [selectedNode, setSelectedNode] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${apiUrl}/tree`);
        const result = await response.json();
        const resultArray = Object.values(result); // Convert dictionary to array
        if (Array.isArray(resultArray)) {
          setData(resultArray);
        } else {
          console.error("Fetched data is not an array:", resultArray);
		  console.log("Api url");
		  console.log(apiUrl);

        }
      } catch (error) {
        console.error("Error fetching data:", error);
		console.log("Api url");
        console.log(apiUrl);
      }
    };

    fetchData();
  }, []);

  const handleNodeClick = (node) => {
    setSelectedNode(node);
  };

  const handleClose = () => {
    setSelectedNode(null);
  };

  return (
    <div className="app">
      <div className="details">
        {selectedNode && (
          <div>
            <button onClick={handleClose}>x</button>
            <h2>{selectedNode.name}</h2>
            <p>{selectedNode.description}</p>
          </div>
        )}
      </div>
      <div className="tree">
        <Tree
          data={treeData}
          onNodeClick={handleNodeClick}
          selectedNode={selectedNode}
        />
      </div>
    </div>
  );
}

export default App;
