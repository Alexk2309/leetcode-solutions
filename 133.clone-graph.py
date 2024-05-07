#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}
        def dfs(node):
            if node in visited: return visited[node]
            nodeClone = Node(node.val)
            visited[node] = nodeClone 
            
            for neighbour in node.neighbors:
                res = dfs(neighbour)
                nodeClone.neighbors.append(res)

            return nodeClone 

        return dfs(node) if node else None
        
# @lc code=end

