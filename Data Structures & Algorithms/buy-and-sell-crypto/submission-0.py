class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0

        max_profit = 0

        for i in range(len(prices)):
            #we can set the max_profit before checking if we need to move left b/c once we move left, we know price will be 0
            #so actually, we can do this in any order b/c if we have to move pointer, it will be negative anyways b/c that means the current price is less than lowest price

            curr_profit = prices[i] - prices[left]
            max_profit = max(max_profit, curr_profit)

            if prices[left] > prices[i]:
                left = i
        return max_profit
        