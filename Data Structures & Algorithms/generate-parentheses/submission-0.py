class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        #put in n for opening and closing out
        def helper(open_count, close_count, curr_list):
            if open_count == 0 and close_count == 0:
                res.append("".join(list(curr_list)))
                return

            #first we need to check if we have opening parenthesis to put down, if we do then add it and backtrack
            if open_count > 0:
                curr_list.append('(')
                open_count -= 1
                helper(open_count, close_count, curr_list)

                curr_list.pop()
                open_count += 1
            
            #can only put down a closing parenthesis if there is a pending opening one that hasn't been closed
            #also need to check if we have closing paranthesis to put down
            if open_count < close_count and close_count > 0:
                curr_list.append(')')
                close_count -= 1

                helper(open_count, close_count, curr_list)

                #backtrack adding the closing paranthesis b/c now we want to try adding an opening one instead
                curr_list.pop()
                close_count += 1
        
        helper(n, n, [])

        return res
        