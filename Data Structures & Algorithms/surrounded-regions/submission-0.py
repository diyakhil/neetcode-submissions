class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()
        edge = set()

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            edge.add((r,0))
            edge.add((r,COLS -1))
        
        for c in range(COLS):
            edge.add((0, c))
            edge.add((ROWS-1, c))
        
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == 'X' or (r,c) in safe:
                return
            
            safe.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r, c in edge:
            dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in safe:
                    board[r][c] = 'X'
        