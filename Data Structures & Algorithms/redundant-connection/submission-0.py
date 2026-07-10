class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        
        #do topological sort to visit each node
        path = []
        visited = set()

        #if we don't make this static then python will declare a new var for the local one
        self.cycle = []
        
        #we have to pass in parent b/c this is undirected graph so it will always go back to parent
        #have to skip over parent in for loop iter

        #need to return if cycle is found
        def dfs(node, parent):
            if node in path:
                indexOfNode = path.index(node)

                #the cycle starts from the curr node to the end, node including any initial nodes that might have occurred before the cycle
                self.cycle = path[indexOfNode:].copy()
                
                return True
            if node in visited:
                return False
            
            path.append(node)
            for child in adj_list[node]:
                if child == parent:
                    continue
                if dfs(child, node):
                    return True
            path.pop()
            
            visited.add(node)
            return False
        
        dfs(1, -1)

        #traversing edge backwards
        for edge in edges[::-1]:
            if edge[0] in self.cycle and edge[1] in self.cycle:
                return edge
        