class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        val_store = dict()

        for index, num in enumerate(nums):

            if num in val_store:
                return True
            
            val_store[num] = index
        
        return False

myClass = Solution()
print(myClass.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))


# the top 4 plans, 