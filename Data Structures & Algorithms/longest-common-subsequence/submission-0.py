class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #got to pad with 0s to make dp cleaner
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for r in range(1, len(text2) + 1):
            for c in range(1, len(text1) + 1):
                if text1[c-1] == text2[r-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        return dp[len(text2)][len(text1)]
        