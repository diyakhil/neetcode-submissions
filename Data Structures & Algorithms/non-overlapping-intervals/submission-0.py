class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)

        last_interval = sorted_intervals[0]
        count = 0

        for i in range(1, len(sorted_intervals)):
            s1 = last_interval[0]
            e1 = last_interval[1]

            curr_interval = sorted_intervals[i]

            s2 = curr_interval[0]
            e2 = curr_interval[1]
            
            #if intervals are overlapping
            if s2 < e1:
                #CORE LOGIC: instead of comparing lengths, compare ends (keep the interval that ends the quickest)
                if e1 > e2:
                    last_interval = curr_interval
                #otherwise just keep whatever last interval is - meaning we aren't counting the current interval
                count += 1
            #this last_interval value needs to be updated to the interval we just 'inserted' if we do not find an overlap
            else:
                last_interval = curr_interval
            
        return count
        