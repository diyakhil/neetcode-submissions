class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        num_to_count = {}
        res = []

        for num in nums:
            num_to_count[num] = num_to_count.get(num, 0) + 1
        
        heap = []
        for key, value in num_to_count.items():
            heapq.heappush(heap, (-value, key))
        
        for i in range(k):
            val = heapq.heappop(heap)
            res.append(val[1])
        return res