class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        # Fast forward to the first window and get the max
        # push the max to the array
        # get the left

        right, left = 0, 0
        window = []
        window_max = nums[0]
        
        while right < k:

            window_max = max(window_max, nums[right])
            right += 1
        
        window.append(window_max)

        # for i in range(left, )

        return window

mySolution = Solution()
print(mySolution.maxSlidingWindow([1, 4, 2, 3, 9], 5))
