class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        #first we can try to find the odd number palindromes
        for i in range(len(s)):
            start = i - 1
            end = i + 1

            palin = s[i]
            length = 1

            if length > res_len:
                res_len = length
                res = palin

            while start >= 0 and end < len(s) and s[start] == s[end]:
                length += 2
                palin = s[start] + palin + s[end]

                if length > res_len:
                    res_len = length
                    res = palin
                
                start -= 1
                end += 1
            
        #then we can try to find even number palindromes (take 2 values as initial word instead of 1), granted they are equal
        for i in range(len(s) -1):
            start = i
            end = i+1

            if s[start] != s[end]:
                continue

            palin = s[i:i+1+1]
            
            length = 2

            if length > res_len:
                res_len = length
                res = palin

            start -= 1
            end += 1

            #make sure start can be 0 so >= 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                
                length += 2
                palin = s[start] + palin + s[end]
                
                if length > res_len:
                    res_len = length
                    res = palin
            
                start -= 1
                end += 1
        
        return res
        