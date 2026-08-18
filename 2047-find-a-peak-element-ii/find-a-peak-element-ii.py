class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])

        left = 0
        right = cols - 1

        while left <= right:
            mid = (left + right) // 2

            # Find maximum element in this column
            max_row = 0

            for r in range(rows):
                if mat[r][mid] > mat[max_row][mid]:
                    max_row = r

            # Check left and right neighbours
            left_val = mat[max_row][mid - 1] if mid > 0 else -1
            right_val = mat[max_row][mid + 1] if mid < cols - 1 else -1

            current = mat[max_row][mid]

            if current > left_val and current > right_val:
                return [max_row, mid]

            elif left_val > current:
                # Peak must be on the left
                right = mid - 1

            else:
                # Peak must be on the right
                left = mid + 1