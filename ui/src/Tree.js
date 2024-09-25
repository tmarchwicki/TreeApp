import React from "react";
import TreeNode from "./TreeNode";

const Tree = ({ data, onNodeClick, selectedNode }) => {
  const buildTree = (nodes, parent) => {
    return nodes
      .filter((node) => node.parent === parent)
      .map((node) => (
        <TreeNode
          key={node.name}
          node={node}
          onNodeClick={onNodeClick}
          selectedNode={selectedNode}
        >
          {buildTree(nodes, node.name)}
        </TreeNode>
      ));
  };

  return <div>{buildTree(data, "")}</div>;
};

export default Tree;
