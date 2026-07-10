class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}
        hash_s = {}

        for c in t:
            hash_t[c] = hash_t.get(c, 0) + 1
            hash_s[c] = 0
        
        min_sub = [-1, -1]
        min_len = float('infinity')

        have = 0
        need = len(hash_t)

        left = 0

        for right in range(len(s)):
            curr_char = s[right]

            if curr_char in hash_t:
                hash_s[curr_char] += 1

                if hash_s[curr_char] == hash_t[curr_char]:
                    have += 1

            while have == need:
                if right - left + 1 < min_len:
                    min_sub = [left, right]
                    min_len = right - left + 1

                # Only decrement if left char is in t
                if s[left] in hash_t:
                    hash_s[s[left]] -= 1
                    if hash_s[s[left]] < hash_t[s[left]]:
                        have -= 1
                
                left += 1
        
        if min_len == float('infinity'):
            return ""
        return s[min_sub[0]:min_sub[1] + 1]
        