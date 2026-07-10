class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        sorted_str_list = defaultdict(list)
        res = []

        for _str in strs:
            sorted_str = "".join(sorted(_str))
            sorted_str_list[sorted_str].append(_str)
        
        for value in sorted_str_list.values():
            res.append(value)

        return res