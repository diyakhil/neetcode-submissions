class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {2:["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5:["j", "k", "l"], 6:["m", "n", "o"], 7:["p", "q", "r", "s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"]}
        if not digits:
            return []
        res = []
        def helper(index, curr_list):

            #base case: if we have as many values as digits in curr_list
            if len(curr_list) == len(digits):
                curr_str = "".join(curr_list.copy())
                res.append(curr_str)
                return
            
            curr_digit = digits[index]

            letters = digit_map[int(curr_digit)]

            #trying out each possible letter for the current number
            for letter in letters:
                curr_list.append(letter)

                helper(index + 1, curr_list)

                curr_list.pop()
        
        helper(0, [])
        return res
        