class Solution:
    def climbStairs(self, n: int) -> int:
        #n+1 b/c we want 0->n as index values
        dp = [0] * (n+1)

        #define base cases
        dp[n] = 0 #dp(5), dp(4), and dp(3) are base cases (5 is answer, 4 and 3 are steps before answer)
        dp[n-1] = 1
        dp[n-2] = 2

        #start from before n-2 and recurse backwards
        for i in range(n - 2 - 1, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]      

        return dp[0]  
        