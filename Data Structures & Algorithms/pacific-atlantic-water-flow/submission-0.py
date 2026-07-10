class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        atlantic_visited = set()
        pacific_visited = set()

        pacific_bordering = set()
        atlantic_bordering = set()

        ROWS = len(heights)
        COLS = len(heights[0])
        
        for c in range(COLS):
            pacific_bordering.add((0, c))
            atlantic_bordering.add((ROWS - 1, c))

        for r in range(ROWS):
            pacific_bordering.add((r, 0))
            atlantic_bordering.add((r, COLS - 1))


        def helper(r, c, isPacific):
            #KEY: bounds are  r<0 not r<= 0
            if isPacific and (r < 0 or r > ROWS or c < 0 or c > COLS or (r,c) in pacific_visited):
                return
            if not isPacific and (r < 0 or r > ROWS or c < 0 or c > COLS or (r,c) in atlantic_visited):
                return
            
            if isPacific:
                pacific_visited.add((r,c))
            else:
                atlantic_visited.add((r,c))
            
            #KEY: check has to be greater than or equal to
            if r+1 < ROWS and heights[r+1][c] >= heights[r][c]:
                helper(r+1, c, isPacific)
            if r-1 >= 0 and heights[r-1][c] >= heights[r][c]:
                helper(r-1, c, isPacific)
            if c+1 < COLS and heights[r][c+1] >= heights[r][c]:
                helper(r, c+1, isPacific)
            if c-1 >= 0 and heights[r][c-1] >= heights[r][c]:
                helper(r, c-1, isPacific)
            
        for r, c in atlantic_bordering:
            helper(r, c, False)
        for r, c in pacific_bordering:
            helper(r, c, True)
        
        res = []
        for pair in atlantic_visited:
            if pair in pacific_visited:
                res.append(pair)
        
        return res
        