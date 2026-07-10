class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #at each step we aren't calculating the min amount of coins across all possible subpaths
        #we are calculating the min number of coins for that specific subproblem
        self.cache = {}
        
        def helper(amount_left):
            #if we have an invalid case, return a large number so it gets disqualified immediately
            if amount_left < 0:
                return float("inf")
            
            if amount_left == 0:
                return 0
            
            if amount_left in self.cache:
                return self.cache[amount_left]
            
            #get min value across all res values when trying each coin
            min_res_value = float("inf")
            for c in coins:
                res = 1 + helper(amount_left - c)
                min_res_value = min(min_res_value, res)
                #don't just return res here b/c we want to compare all subproblems for the amount and then return the min one
            
            #cache the min value of coins for this subproblem
            self.cache[amount_left] = min_res_value
            return min_res_value
            
        helper(amount)
        
        if amount == 0:
            return 0

        if self.cache[amount] == float("inf"):
            return -1
        return self.cache[amount]
        
        