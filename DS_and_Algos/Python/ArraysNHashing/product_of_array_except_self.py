class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
       res = [1] * (len(nums))

       prefix = 1

       for i, val in enumerate(nums):
           res[i] = prefix
           prefix *= val

       postfix = 1
       for j in range(len(nums) -1, -1, -1):
        res[j] *= postfix
        postfix *= nums[j]

       print("prefix is: ", res)

myClass = Solution()
myClass.productExceptSelf([-1, 1, 0, -3, 3])
