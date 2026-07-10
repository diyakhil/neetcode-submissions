class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #don't need an adj_list
        #do need a weights array

        weights = [float('inf')] * n

        #need this to start indicate src is the starting point, without this all the weights will just be inf b/c inf + any value is inf
        weights[src] = 0
        for _ in range(k+1):
            #KEYYY: relaxing an edge in this iteration should actually be used for the next one
            #for this reason, we need a copy for the current weights array so to not influence the next
            #iteration's edges in this one
            curr_weights = weights.copy()

            for flight in flights:
                start, end, price = flight

                #return early if start is inf b/c everything else will be inf then
                if curr_weights[start] == float('inf'):
                    continue

                #weight of prev place + curr price has to be less than curr weight of end
                if curr_weights[start] + price < weights[end]:
                    weights[end] = curr_weights[start] + price
        
        if weights[dst] == float('inf'):
            return -1
        else:
            return weights[dst]
        