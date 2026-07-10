class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for i in range(len(points)):
            distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            heapq.heappush(heap, (distance, i))
        
        res = []
        for i in range(k):
            distance, index = heapq.heappop(heap)
            res.append(points[index])
        
        return res
        