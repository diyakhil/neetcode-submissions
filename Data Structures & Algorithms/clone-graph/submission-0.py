"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        og_to_new = {}

        def dfs(node):
            if not node:
                return
            #base case: if node already exists in map return it right away
            if node in og_to_new.keys():
                return og_to_new[node]

            new_node = Node(node.val)
            og_to_new[node] = new_node

            new_node_neighbors = []

            for neighbor in node.neighbors:
                new_node_neighbors.append(dfs(neighbor))
            
            new_node.neighbors = new_node_neighbors

            #need to return new_node at the end b/c other recursive calls are depending on a node being returned at each step
            return new_node
        
        return dfs(node)
        