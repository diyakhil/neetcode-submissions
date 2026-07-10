class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        #we are populating the indices from start to end b/c we can either start on the 1st or 2nd step
        #the base cases will be the first 2 cost values
        dp[0] = cost[0]
        dp[1] = cost[1]

        #populate the rest of the dp array by taking the min of the previous steps + the cost of the curr step
        #this value will be used in the rest of the calculates down the array since we want the cost at that particular step
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        #since the last step has no cost, we don't need to add the cost, we can simply take the min of the last 2 array elems
        return min(dp[len(cost) - 1], dp[len(cost) -2])
        