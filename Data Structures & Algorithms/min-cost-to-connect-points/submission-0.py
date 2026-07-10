class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #need to generate all the possible edges between vertices in this graph
        #min heap to store weight and edges

        minheap = []
        for i in range(len(points)):
            #add one b/c we don't want to compare the same points
            for j in range(i+1, len(points)):
                p1 = points[i] #(x1, y1)
                p2 = points[j] #(x2, y2)

                distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

                #just use i and j as the node values since none are given to us
                heapq.heappush(minheap, [distance, i, j])
        
        #have to do union find, start with smallest edge, check corresponding nodes belong in the same set
        #if they do then skip, if they don't then union and combine them
        #keep unioning until we get all the nodes in one set

        #declare a parent array to keep track of the parent node of all the nodes
        #set value to -1 at first to show each node is it's own parent to start with
        parent = [-1] * len(points)

        #make helpers for union and find
        def find(node):
            #KEY: I needed to return the parent before we reached -1
            while parent[node] > -1:
                node = parent[node]
            return node
        
        def union(node1, node2):
            #have to run a find in union
            parent1 = find(node1)
            parent2 = find(node2)
            #only union if do not belong to same parent

            if parent1 != parent2:
                parent[parent2] = parent1
                return True
            else:
                return False
        
        sum_edges = 0
        edges_count = 0
        #to connect all the nodes, we need n-1 edges
        while edges_count < len(points) - 1:
            if minheap:
                distance, p1, p2 = heapq.heappop(minheap)

                if union(p1, p2):
                    sum_edges += distance

                    edges_count += 1
        
        return sum_edges