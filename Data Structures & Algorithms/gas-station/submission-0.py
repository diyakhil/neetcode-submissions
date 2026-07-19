class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #this tells you whether an answer exists at all
        if sum(gas) < sum(cost):
            return -1
        
        #if we reached this point that means one valid answer exists
        #let's compute a gas-cost array to see the total gain or burden from moving from one station to the other
        gas_minus_cost = []

        for i in range(len(gas)):
            total = gas[i] - cost[i]
            gas_minus_cost.append(total)
        
        acc = 0
        start = 0
        all_positive = False
        for i in range(len(gas_minus_cost)):
            acc += gas_minus_cost[i]

            #if we ever reach a negative, we will rule out that station and start from 0 again
            if acc < 0:
                acc = 0
                #reset start b/c start can only be pointing to the start of a subarray that's all positive
                #can't go negative in the later half
                all_positive = False
            #the first index to make acc greater than 0 
            if acc > 0 and all_positive == False:
                all_positive = True
                start = i

        return start
        