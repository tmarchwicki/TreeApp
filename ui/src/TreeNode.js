import React from "react";

const TreeNode = ({ node, onNodeClick, selectedNode, children }) => {
  const isSelected = selectedNode && selectedNode.name === node.name;

  return (
    <div className="tree-node-container">
      <div className={`tree-node ${isSelected ? "selected" : ""}`}>
        <span onClick={() => onNodeClick(node)}>{node.name}</span>
        <button className="close-btn" onClick={() => onNodeClick(null)}>
          x
        </button>
      </div>
      {children && <div className="children">{children}</div>}
    </div>
  );
};

export default TreeNode;
