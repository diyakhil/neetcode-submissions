class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.cache = {}

        def dfs(i, have_coin, prev_sell):
            #if we have reached the last day, then add the profit calculated to the array and return
            if i == len(prices):
                return 0

            if (i, have_coin, prev_sell) in self.cache:
                return self.cache[(i, have_coin, prev_sell)]
            
            #if we sold at the previous turn, we have no choice but to cooldown
            if prev_sell:
                result = dfs(i+1, False, False)

            #we have 2 options if we have don't have the coin, we can either buy or cooldown
            elif not have_coin:
                buy = dfs(i+1, True, False) - prices[i]
                cooldown = dfs(i+1, False, False)
                result = max(buy, cooldown)
            
            #we have 2 options if we have the coin, we can either sell or cooldown
            else:
                sell = dfs(i+1, False, True) + prices[i]
                cooldown = dfs(i+1, True, False)
                result = max(sell, cooldown)
            
            #cache and return reseult at the end
            self.cache[(i, have_coin, prev_sell)] = result
            return result
        
        return dfs(0, False, False)