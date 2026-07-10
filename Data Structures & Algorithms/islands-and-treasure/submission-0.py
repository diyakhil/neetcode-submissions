class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = collections.deque() #use a deque instead of a reg list for performance

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        counter = 0
        visited = set()

        while queue:
            curr_squares = len(queue)

            for _ in range(curr_squares):
                r, c = queue[0]
                
                #need to check bounds for r, c
                if r >= 0 and c >= 0 and r < ROWS and c < COLS and (r,c) not in visited and grid[r][c] != -1:
                    grid[r][c] = counter

                    visited.add((r,c))

                    #add neighbors to queue
                    queue.append((r+1, c))
                    queue.append((r-1, c))
                    queue.append((r, c+1))
                    queue.append((r, c-1))
                
                #need to pop from queue regardless, just don't go further with the ones that don't meet condition above
                queue.popleft()
                
            counter += 1
        