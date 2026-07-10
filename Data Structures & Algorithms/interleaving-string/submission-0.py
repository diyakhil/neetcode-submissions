class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.cache = {}
        #recursive solution first with memoization
        def helper(i, j, k):
            if k >= len(s3):
                #need to check if all letters are used before returning
                return i >= len(s1) and j >= len(s2)
            if (i, j, k) in self.cache:
                return self.cache[(i, j, k)]
            
            res1 = False
            res2 = False

            if i < len(s1) and s1[i] == s3[k]:
                res1 = helper(i+1, j, k+1)
            if j < len(s2) and s2[j] == s3[k]:
                res2 = helper(i, j+1, k+1)
            
            self.cache[(i, j, k)] = res1 or res2
            return res1 or res2
        
        return helper(0, 0, 0)