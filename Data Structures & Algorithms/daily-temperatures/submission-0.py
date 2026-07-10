class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input: int array of temps
        #output: num of days at each position you have to wait for the temps to get warmer

        stack = [] #store (temp, index) in here
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            #this needs to be a while loop since we need to pop ALL prev temps that are lower than the current one
            while stack and stack[-1][0] < temperatures[i]:
                #handle logic for popping smaller value from stack and updatinhg result array
                temp, index = stack.pop()
                res[index] = i - index
            #we push the curr value into the stack regardless of whether we popped or not
            stack.append((temperatures[i], i))
        
        return res
        