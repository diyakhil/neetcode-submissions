class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #input: array of ints piles where piles[i] is the number of bananas in pile i and h which is the
        #number of hours koko has to eat those bananas

        #output: minimum bananas per hour speed, k, such that koko can eat all the bananas within h hours

        #left and right are the amount of bananas per hour not the hours themselves
        left = 1
        right = max(piles)

        #the maximum rate is the biggest pile b/c if she can eat that in an hour, she can eat the rest
        min_rate = max(piles)

        while left <= right:
            mid = (left + right) // 2

            total_hours = 0
            for pile in piles:

                #have round up b/c even if we finish within the hour, we cannot move on
                pile_hours = math.ceil(pile / float(mid))
                total_hours += pile_hours
            
            if total_hours <= h:
                min_rate = min(min_rate, mid)
                right = mid - 1
            else:
                #we can't update min_rate in this case b/c we did not choose a valid rate (did not fall under hours)
                left = mid + 1
        
        return min_rate
        