class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(height, index)
        max_value = 0 # running max that we will need to keep track of

        for i in range(len(heights)):
            new_index = -1
            while stack and heights[i] <= stack[-1][0]:
                #take care of the case where we want to add a smaller value to the stack than what we have in the stack
                height, index = stack.pop()
                #update max_value with what could have been the area with the popped value

                area = (i - index) * height
                
                max_value = max(max_value, area)
                
                new_index = index
            
            if new_index == -1:
                new_index = i
            
            #add item to stack, take care of the case where this histogram * 1 could be the max va;
            stack.append((heights[i], new_index))
            max_value = max(max_value, heights[i])
        
        #now we need to take care of the case where the stack is still full, this will happen in a case like
        #1, 5, 6 -> all of these are ascending in which case we will never pop from the stack

        while stack:
            height, index = stack.pop()
            #since we know that these are the only histograms left, we know the ending index must be last index in heights
            #because everything is going to the end now

            #need to use len(heights) here NOT len(heights) - 1 b/c teh rectangle extends up to but not including the final index
            len_heights = len(heights)

            area = (len_heights - index) * height
            max_value = max(max_value, area)
        
        return max_value
        