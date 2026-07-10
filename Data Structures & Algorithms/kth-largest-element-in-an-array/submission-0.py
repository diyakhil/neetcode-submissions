class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min heap for this problem
        #adding all the values to the heap and then removing them is NOT optimal, keep pruning the heap when greater than k so the time complexity is lower (logk instead of logn b/c the list will never get to n nodes)
        minheap = []

        for num in nums:
            heapq.heappush(minheap, num)
            
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        return minheap[0]
        