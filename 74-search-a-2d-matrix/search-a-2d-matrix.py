class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols -1

        while left <= right :
            mid = left + (right - left) // 2

            #getting the row idx
            rowIdx = mid // cols #to find in which row element is 
            colIdx = mid % cols #to find in which col element is

            if matrix[rowIdx][colIdx] == target:
                return True
            elif matrix[rowIdx][colIdx] < target:
                left = mid + 1
            else:
                right = mid -1

        return False