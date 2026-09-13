class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)

        final_intervals = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            prev_interval = final_intervals[-1]
            curr_interval = sorted_intervals[i]

            s1 = prev_interval[0]
            s2 = prev_interval[1]

            e1 = curr_interval[0]
            e2 = curr_interval[1]

            #if intervals overlap
            if e1 <= s2:
                final_intervals.pop()
                new_interval = [s1, max(s2, e2)]

                final_intervals.append(new_interval)
            else:
                final_intervals.append(curr_interval)
            
        return final_intervals
        