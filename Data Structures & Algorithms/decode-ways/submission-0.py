class Solution:
    def numDecodings(self, s: str) -> int:
        #KEY: ADD MEMOIZATION TO THE RECURSIVE SOL
        memo = {}
        
        def helper(s):
            #check if we already computed substring in another go
            #NOTICE HOW WE RETURN EARLY IF WE ALR HAVE COMPUTED, THIS IS THE DP STEP
            if s in memo:
                return memo[s]
            
            if s == "":
                return 1
            
            if s == "0":
                return 0
            
            first_int = s[0]
            first_two_int = s[0:2]

            if first_int == "0":
                return 0

            #need to make sure that 2 chars actually exist to go into else case
            if int(first_two_int) > 26 or len(first_two_int) < 2:
                result = helper(s[1:])
            else:
                result = helper(s[1:]) + helper(s[2:])
            #save the result of the recursion associated with the substring
            memo[s] = result
            return result

        return helper(s)
        