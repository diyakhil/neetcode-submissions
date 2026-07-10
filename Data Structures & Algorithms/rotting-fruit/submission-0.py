class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
        time = -1
        while queue:
            curr_rotten = len(queue)

            for _ in range(curr_rotten):
                r,c = queue.popleft()

                if r+1 < ROWS and grid[r+1][c] == 1:
                    queue.append((r+1, c))
                    grid[r+1][c] = 2
                
                if r-1 >= 0 and grid[r-1][c] == 1:
                    queue.append((r-1, c))
                    grid[r-1][c] = 2
                
                if c+1 < COLS and grid[r][c+1] == 1:
                    queue.append((r, c+1))
                    grid[r][c+1] = 2
                
                if c-1 >= 0 and grid[r][c-1] == 1:
                    queue.append((r, c-1))
                    grid[r][c-1] = 2
            
            time += 1
    
        for arr in grid:
            if 1 in arr:
                return -1
        else:
            return max(0, time)
        