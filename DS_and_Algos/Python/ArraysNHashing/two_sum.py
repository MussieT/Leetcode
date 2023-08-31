class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        store = {}

        for index, val in enumerate(nums):

            remaining = target - val

            if remaining in store:
                return [store[remaining], index]
            
            store[val] = index
            
myClass = Solution()
print(myClass.twoSum([1, 2, 3], 9))