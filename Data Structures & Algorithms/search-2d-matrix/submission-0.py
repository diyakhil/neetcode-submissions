class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        ROW = len(matrix)
        COL = len(matrix[0])

        #declare left pointer on starting point of the top row
        #declare right pointer on the ending point of top row
        left = [0, 0]
        right = [0, COL - 1]

        #iterate until we are out of columns to move to
        while left[0] < ROW:

            #target is greater than last value in this row, we have to move onto next row
            if target > matrix[right[0]][right[1]]:
                left = [left[0] + 1, left[1]]
                right = [right[0] + 1, right[1]]
            #the target is within this row
            elif target >= matrix[left[0]][left[1]] and target <= matrix[right[0]][right[1]] and left[0] == right[0] and left[1] <= right[1]:
                row = left[0]
                #now we just need to use col values to find the median
                mid = (left[1] + right[1]) // 2
                
                if matrix[row][mid] > target:
                    right[1] = mid - 1
                elif matrix[row][mid] < target:
                    left[1] = mid + 1
                else:
                    return True
            else:
                return False
        return False
        