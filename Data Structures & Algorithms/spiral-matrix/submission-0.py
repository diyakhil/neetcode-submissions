class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        rows = len(matrix)
        cols = len(matrix[0])

        L = 0
        R = cols

        T = 0
        B = rows

        curr_row = 0
        curr_col = 0

        while L < R and T < B:

            #top row
            for i in range(L, R):
                result.append(matrix[T][i])
            T += 1

            #right col
            for i in range(T, B):
                result.append(matrix[i][R - 1])
            R -= 1

            if not (L < R and T < B):
                break

            #bottom row
            for i in range(R - 1, L - 1, -1):
                result.append(matrix[B - 1][i])
            B -= 1

            #left col
            for i in range(B - 1, T - 1, -1):
                result.append(matrix[i][L])
            L += 1
        
        return result
        