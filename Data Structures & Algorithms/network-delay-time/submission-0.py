class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #need visited set, adjacency list (keep track of adjacent nodes), and weights list

        visited = set()
        weights = [float('inf')] * n #set all weights to infinity to start with
        adj_list = defaultdict(list)

        #KEY: use a min heap instead of list for BFS
        heap = []

        weights[k - 1] = 0
        heapq.heappush(heap, [0, k])

        for time in times:
            #need to append this b/c multiple edges can start from the same source node
            adj_list[time[0]].append([time[1], time[2]])
        
        #while we haven't visited every node
        while len(visited) < n and heap:
            #KEY: need to keep checking if heap is there
            #KEY: need to skip over nodes that have already been visited because the heap will contain incorrect weightage values for them
            while heap and heap[0][1] in visited:
                heapq.heappop(heap)
            
            if not heap:
                break
            curr_weight, curr_node = heapq.heappop(heap)
            visited.add(curr_node)

            #look at all adjacent nodes to popped node
            for target_node, weight in adj_list[curr_node]:
                if curr_weight + weight < weights[target_node - 1]:
                    weights[target_node - 1] = curr_weight + weight
                    heapq.heappush(heap, [curr_weight + weight, target_node])
        
        #if there's an infinity left that means some nodes are unreachable
        if max(weights) == float('inf'):
            return -1
        else:
            return max(weights)
        