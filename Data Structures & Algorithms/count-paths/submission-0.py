class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #m is rows and n is cols
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]
        