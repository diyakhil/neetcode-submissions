class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #create an adj list 2 ways cuz the graph is not connected
        adj_list = defaultdict(list)

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        visited = set()
        #I don't think we need to set a path var here b/c we don't care about cycles since we just return if in visited
        #just need to keep track of the nodes we see in this part of the graph
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            for child in adj_list[node]:
                dfs(child)
        
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        return components
        