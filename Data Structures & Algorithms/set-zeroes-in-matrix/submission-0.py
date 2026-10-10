class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        #keep track of which rows and columns to zero out while traversing the matrix
        rows_to_zero = set()
        cols_to_zero = set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_to_zero.add(r)
                    cols_to_zero.add(c)
        
        #actually zero out those rows and cols
        for r in rows_to_zero:
            for c in range(cols):
                matrix[r][c] = 0
        
        for c in cols_to_zero:
            for r in range(rows):
                matrix[r][c] = 0
        
        