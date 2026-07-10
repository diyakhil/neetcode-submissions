class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        #visited keeps track of all the squares visited in the current iteratoon
        visited = set()

        ROWS = len(board)
        COLS = len(board[0])

        #r,c will represent the current square we are on
        #index will traverse the word and keep track of which letter we need to track on the board
        def helper(r, c, index):
            #now we are actually checking the last index in the board, we need another iteration to check len(word) -1 index
            if index == len(word):
                return True
            
            #have to check upper and lower limit
            if r >= ROWS or c >= COLS or c < 0 or r < 0 or (r,c) in visited or board[r][c] != word[index]:
                return False
            
            visited.add((r,c))

            #recurse in all 4 directions with next char in word
            #KEY: NEED TO GET RESULT OF RECURSIVE FUNCTION OR THERE WILL BE NOTHING TO BUILD ON
            #ors b/c only one path needs to return true
            #DO NOT RETURN HERE b/c backtracking step will never be reached, just record the res and return after backtracking
            res = helper(r-1, c, index+1) or helper(r+1, c, index+1) or helper(r, c+1, index+1) or helper(r, c-1, index+1)

            #backtrack b/c not necessary that this square will be included in the solution, could go a diff direction
            visited.remove((r,c))
            return res
        
        #we need to go through each square now for the solution
        for i in range(ROWS):
            for j in range(COLS):
                res = helper(i, j, 0)

                if res:
                    return True
        return False