class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # base case 1, if array contains one element, return it
        # The Trick - compare the nearest integer, go to the biggest integer

        n = len(nums)
        left, right = 0, n - 1

        if n == 1:
            return 0

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            
            else:
                right = mid - 1

ExampleSolution = Solution()
print(ExampleSolution.findPeakElement([1,2]))
