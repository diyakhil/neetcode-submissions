class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        #this represent cols
        L = 0
        R = cols - 1

        T = 0
        B = rows - 1
        
        result = []
        #while these pointers don't collide
        while L <= R and T <= B:
            #use for loops here instead of a while loop, we know we need to loop L -> R first for the top row
            for i in range(L, R + 1):
                result.append(matrix[T][i])
            #increment top right after since we have alreadu explored that row
            T += 1
            
            #now we will go top to bottom on the right side
            for i in range(T, B + 1):
                result.append(matrix[i][R])
            R -= 1

            if not (L <= R and T <= B):
                break

            for i in range(R, L - 1, -1):
                result.append(matrix[B][i])
            B -= 1

            for i in range(B, T - 1, -1):
                result.append(matrix[i][L])
            L += 1
        return result