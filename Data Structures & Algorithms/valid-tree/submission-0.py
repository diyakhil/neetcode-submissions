class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = defaultdict(list)

        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])
        
        path = set()
        visited = set()

        def dfs(node, parent):

            if node in path:
                return False

            #add curr node to path
            path.add(node)
            
            for child in adj_map[node]:
                #KEY: we don't want to recurse if child = parent b/c we are exploring the second way of the connection
                #since this is an undirected graph, each edge goes both ways (see recursive tree for example)
                if child == parent:
                    continue
                
                if not dfs(child, node):
                    return False
            
            path.remove(node)
            visited.add(node)
            return True
        
        #ONLY NEED 1 dfs call b/c 1 will go through whole tree if connected
        # for i in range(n):
        #     if not dfs(i, -1):
        #         return False
            
        #     if len(visited) != n:
        #         return False

        if not dfs(0, -1):
            return False
            
        if len(visited) != n:
            return False
        return True
        