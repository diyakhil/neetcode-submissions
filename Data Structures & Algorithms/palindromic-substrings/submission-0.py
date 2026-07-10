class Solution:
    def countSubstrings(self, s: str) -> int:
        palins = 0

        #adds odd number palindromes (1 element in the middle)
        for i in range(len(s)):
            start = i - 1
            end = i + 1

            palins += 1

            while start >= 0 and end < len(s) and s[start] == s[end]:
                palins += 1
                
                start -= 1
                end += 1
        
        #adds even number palindrome (2 elements in the middle)
        #middle values will contain curr value and next so we need to stop one before end
        for i in range(len(s) - 1):
            
            #if middle 2 elements are not equal, it cannot be a palindrome
            if s[i] != s[i+1]:
                continue
            
            palins += 1

            start = i - 1
            #i+1 will be the ending value in palin
            end = i + 2

            while start >= 0 and end < len(s) and s[start] == s[end]:

                palins += 1

                start -= 1
                end += 1
        
        return palins

        #KEY: don't actually have to keep track of the palindrome here, just need to add to palindrome when current value
        #is a palindrome
        