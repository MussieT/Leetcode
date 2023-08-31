class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        # steps.
            # 1. start from left - as 1.
            # 2. add numbers till >= target.
            # 3. If target is found .. move the left.
            # 4. keep the min distance between left and right (right - left + 1)
            # 5. If the new sum is not >= target, then move the right

        left, minSubArrayLength = 0, float('inf')
        totalSum = 0
        
        for right in range(len(nums)):

            totalSum += nums[right]

            # IMPORTANT (iterate after total sum is found - NOT to find the total sum ) -> think in reverse order
            while totalSum >= target:
                minSubArrayLength = min(minSubArrayLength, right - left + 1)
                totalSum -= nums[left]
                left += 1

        if minSubArrayLength == float("inf"):
            return 0
        
        return minSubArrayLength

myClass = Solution()
print(myClass.minSubArrayLen(3, [1, 1, 1, 1]))
