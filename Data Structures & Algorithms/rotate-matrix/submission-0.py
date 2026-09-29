class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row_to_vals = {}

        #go column by column
        for c in range(cols):
            vals = []
            for r in range(rows):
                vals.append(matrix[r][c])
            vals.reverse()
            row_to_vals[c] = vals
        #now we have a list of the row number (each column becomes the rows) and then contents in the
        #order it is supposed to go in the row

        #now we will modify the original array with these values
        for r, vals in row_to_vals.items():
            for c in range(cols):
                #vals is just a list (represents the first row) and each value in that list is the col spot its supposed to go in
                matrix[r][c] = vals[c]
        