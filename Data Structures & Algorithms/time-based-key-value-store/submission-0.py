class TimeMap:

    def __init__(self):
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        _list = self.time_map[key]
        left = 0
        right = len(_list) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if _list[mid][0] == timestamp:
                return _list[mid][1]
            elif timestamp > _list[mid][0]:
                left = mid + 1
            else:
                right = mid - 1
        
        if left - 1 < 0: return ""
        else: return _list[left-1][1]