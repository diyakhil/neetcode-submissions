class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def helper(amount, coin_index):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            
            if (amount, coin_index) in cache:
                return cache[(amount, coin_index)]
            
            total = 0

            for i in range(coin_index, len(coins)):
                new_amount = amount-coins[i]
                
                #we are using i here because they cannot use any coins before the index we are currently on
                #to prevent duplicate combos since we want the combinations not permutations

                #we use i instead of i+1 because they can reuse the index they currently are on
                total += helper(new_amount, i)

            cache[(amount, coin_index)] = total
            return total
        
        return helper(amount, 0)
        