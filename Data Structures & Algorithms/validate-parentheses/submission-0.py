class Solution:
    def isValid(self, s: str) -> bool:
        #map each closing parenthesis with an opening one

        #maintain a stack and keep pushing into it until we reach a closing paranthesis
        #when we reach the closing, pop from the stack and make sure popped value is the corresponding opening one

        p_map = {'}': '{', ']': '[', ')': '('}
        stack = []

        for c in s:
            #if opening
            if c in p_map.values():
                stack.append(c)
            elif c in p_map.keys() and stack:
                prev = stack.pop()

                if prev != p_map[c]:
                    return False
            else:
                return False
        #now we need to make sure stack is empty, if it is return true (all closing have corresponding opening)
        if len(stack) == 0: return True
        else: return False
        