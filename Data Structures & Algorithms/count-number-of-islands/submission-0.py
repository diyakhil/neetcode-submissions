class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #KEY: all of the 1 and 0s are STRINGS not INTS
        #for graph dfs use r+-1 and c+-1 for the "next" values

        #idea here is we need to explore all of the land connecting to one island and mark all of the r,c pairs as visited
        #SO when we try to discover a new island, we aren't accidentally looking at another island's land

        #need a global visited set value b/c we don't want this to be diff across recursion
        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c): #think we just need r,c here
            #the point of this is to just add to visited so when we iterate over each row, col we know when to increment islands
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r,c) in visited:
                return
            
            visited.add((r,c))

            #don't need to return anything from the recursion b/c we aren't expecting result from recursion
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        

        numIslands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1": #KEY: have to add the check here if it's an island (1)
                    numIslands += 1
                    dfs(r,c)
        return numIslands
        