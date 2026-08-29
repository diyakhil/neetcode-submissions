class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #first iter = insert

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                #once we haveb inserted the interval we don't need to continue
                break
        if newInterval not in intervals:
            intervals.append(newInterval)
        
        #second iter = merge duplicates
        #need to do a while loop here because contents are shifting
        if intervals:
            new_list = [intervals[0]]
        else:
            intervals.append(newInterval)
            return intervals
        for i in range(1, len(intervals)):
            #check if overlapping with the last value in new_list
            e1 = new_list[-1][1]
            s2 = intervals[i][0]
            if e1 >= s2:
                #pop out the last value b/c intervals are overlapping
                prev_value = new_list.pop()
                e2 = intervals[i][1]

                new_end = max(e1, e2)

                s1 = prev_value[0]
                new_value = [s1, new_end]
                new_list.append(new_value)
            else:
                #we can safely push the current value if nothing overlaps
                new_list.append(intervals[i])
        
        return new_list

        