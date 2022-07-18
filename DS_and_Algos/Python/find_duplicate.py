class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicateCompare = dict()
        
        for i, num in enumerate(nums):
            if(num in duplicateCompare):
                return num
            else:
                duplicateCompare[num] = i