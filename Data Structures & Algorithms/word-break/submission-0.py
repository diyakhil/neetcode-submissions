class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        #base case value needs to be true because if the word ends up to there and is in the substring
        #then this j value needs to return true because there is nothing before the word

        #remember dp[j] keeps track of if the word before this char exists in wordDict
        #since there is nothing before s[0] this needs to be true
        dp[0] = True

        #need to iterate to one over because string concat is exclusive
        for i in range(1, len(s) + 1):

            #iterate backwards from i to 0
            for j in range(i - 1, -1, -1):

                #substring is in wordDict and the string that exists before up to j is also in wordDict
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
            if dp[i]:
                continue
            else:
                dp[i] = False
        
        return dp[len(s)]
        