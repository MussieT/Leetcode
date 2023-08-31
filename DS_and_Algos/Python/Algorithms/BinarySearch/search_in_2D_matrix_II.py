class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
      
        for row in range(len(matrix)):

            print("row: ", row)

            left = 0
            right = len(matrix[row]) - 1

            print("right : ", right)

            while left <= right:
               
               mid = (left + right) // 2

               if matrix[row][mid] == target:
                   return True
               
               elif matrix[row][mid] < target:
                   left = mid + 1
                
               else:
                   right = mid - 1
                
        return False

ExampleSolution = Solution()
print(ExampleSolution.searchMatrix(
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5
    )
)
