class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        cols, rows, m = len(matrix), len(matrix[0]), len(matrix[0]) - 1
        left, right = 0, cols - 1

        # search where the number belongs
        while left < right:

            mid = (left + right) // 2

            if matrix[mid][m] < target:
                left = mid + 1
            
            else:
                right = mid

        targetIndex = right
        left, right = 0, rows - 1

        # search through the founded matrix
        while left <= right:

            mid = (left + right) // 2

            if matrix[targetIndex][mid] == target:
                return True

            if matrix[targetIndex][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        
ExampleSolution = Solution()
print(ExampleSolution.searchMatrix(
   [[1],[3]], 1
    )
)