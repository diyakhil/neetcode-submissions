class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            heavier = -1 * heapq.heappop(heap)
            heavy = -1 * heapq.heappop(heap)

            if heavier > heavy:
                diff = heavier - heavy
                heapq.heappush(heap, -diff)
        
        if heap:
            return -1 * heap[0]
        else:
            return 0