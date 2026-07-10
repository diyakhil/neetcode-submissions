class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #first we need to count our frequency

        letter_freq = {}

        for task in tasks:
            if letter_freq.get(task):
                letter_freq[task] += 1
            else:
                letter_freq[task] = 1
        
        heap = []

        for value in letter_freq.values():
            heapq.heappush(heap, -value)
        
        queue = []
        time = 0

        while heap or queue:

            if heap:
                freq = heapq.heappop(heap) * -1
                time += 1

                if freq > 1:
                    queue.append((freq - 1, time + n))

            #first value of queue is the most recent coordinate inserted and the second value of
            #the coordinate is time at which it is available
            while queue and queue[0][1] == time:

                #pop from the front of the queue
                freq, time = queue.pop(0)

                #add frequency back to heap
                heapq.heappush(heap, -freq)
            
            if not heap and queue and queue[0][1] > time:
                time += 1
        
        return time
        