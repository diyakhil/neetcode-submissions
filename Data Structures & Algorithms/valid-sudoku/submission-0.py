class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        ROWS = COLS = 9

        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for i in range(ROWS):
            for j in range(COLS):
                #need to account for the . case
                if board[i][j] == '.':
                    continue

                if board[i][j] in row_set[i] or board[i][j] in col_set[j] or board[i][j] in box_set[(i // 3, j // 3)]:
                    return False
                
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                box_set[(i // 3, j // 3)].add(board[i][j])
        return True