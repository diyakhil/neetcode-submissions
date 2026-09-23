"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda i: i.start)
        if not sorted_intervals:
            return True
        last_interval = sorted_intervals[0]

        for i in range(1, len(sorted_intervals)):

            curr_interval = sorted_intervals[i]

            #intervals are overlapping
            if curr_interval.start < last_interval.end:
                return False
            
            last_interval = curr_interval
        return True