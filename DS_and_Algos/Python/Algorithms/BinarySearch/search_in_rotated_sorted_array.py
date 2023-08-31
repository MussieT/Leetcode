class Solution:
    def search(self, nums: list[int], target: int) -> int:

          # Scenarios,

            # If target is less than or equal to the middle (PERFECT)
                # If left is less than the target and right is less than the left, go left                             
                # else, go right
            
            # If target is greater than middle
                # If right is less than target and middle is less than right
        
        # [4, 5, 6, 7, 0, 1, 2, 3]
        # [3, 4, 5, 6, 7, 1, 2]
        # [7, 1, 2, 3, 4]

        n = len(nums)
        left, right = 0, n - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif target <= nums[mid]:
                
                if nums[left] <= target and nums[right] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:

                if nums[right] <= target and nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


ExampleSolution = Solution()
print(ExampleSolution.search([7, 0, 1, 2, 3], 0))