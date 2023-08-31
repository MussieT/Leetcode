class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int):

        store = dict()
        
        for index in range(len(nums)):

            if nums[index] in store and index - store[nums[index]] <= k:
                return True
            
            store[nums[index]] = index
        
        return False

myClass = Solution()
print(myClass.containsNearbyDuplicate([1, 2, 3, 1], 2))