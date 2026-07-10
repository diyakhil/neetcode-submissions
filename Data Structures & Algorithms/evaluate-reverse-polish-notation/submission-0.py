class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #input = array of tokens in Reverse Polish notation
        #output = single int answer of the result of the arithmetic

        #every time we reach an operator, we pop the next 2 numbers from the stack and use that operator to evaluate our function and update our total
        operations = ['-', '+', '/', '*']
        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                val1 = int(stack.pop())
                val2 = int(stack.pop())

                if token == '+':
                    res = val1 + val2
                if token == '-':
                    res = val2 - val1
                if token == '*':
                    res = val1 * val2
                if token == '/':
                    res = int(val2 / float(val1))
                
                stack.append(res)
        return int(stack[0])
        