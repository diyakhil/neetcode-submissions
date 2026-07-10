class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.cache = {}

        def helper(i, j):
            if i >= len(word1):
                #KEY: missed this the first time, when i has been exhausted but j has not reached the end, return the remaining chars left in j, this is the number of additions we will need to do
                return len(word2[j:])
            
            if (i, j) in self.cache:
                return self.cache[(i, j)]

            if j < len(word2) and word1[i] == word2[j]:

                res = helper(i+1, j+1)
                self.cache[(i, j)] = res
                return res
            
            else:
                #replace: i+1, j+1
                #delete: i+1, j
                #insert: i, j+1

                #need to init these to large values not 0 b/c then that path will be chosen in unassigned
                replace = float("inf")
                delete = float("inf")
                insert = float("inf")

                if (j+1 <= len(word2)):
                    replace = 1 + helper(i+1, j+1)
                    insert = 1 + helper(i, j+1)
                delete = 1 + helper(i+1, j)

                res = min(replace, insert, delete)
                self.cache[(i, j)] = res
                return res
        
        return helper(0, 0)
        