"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts = sorted(starts)
        ends = sorted(ends)

        count = 0
        max_count = 0

        while ends:
            if starts and starts[0] < ends[0]:
                starts.pop(0)
                count += 1
                max_count = max(max_count, count)
            else:
                ends.pop(0)
                count -= 1
        return max_count
        