import React from 'react';

function NodeDetails({ selectedNode, onClose }) {
  if (!selectedNode) return null;

  return (
    <div className="node-details">
      <button className="close-button" onClick={onClose}>x</button>
      <h2>{selectedNode.name}</h2>
      <p>{selectedNode.description}</p>
    </div>
  );
}

export default NodeDetails;