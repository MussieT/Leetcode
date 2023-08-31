class Solution:
    def findMin(self, nums: list[int]) -> int:
        # If the middle is equal to both the firs and the last, add 1 to left , subtract 1 from the right
        # Since there will be two independently sorted sub arrays, find the smallest one
        # If middle is greater than the right, go right
        # If the middle is less than the right, go left

        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            print(f"mid is {mid}, right is {right} and left is {left}")

            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            
            elif nums[left] <= nums[mid] and nums[left] <= nums[right]:
                left = mid - 1
            
            else:
                right = mid + 1

ExampleSolution = Solution()
print(ExampleSolution.findMin([3, 3, 1, 3]))