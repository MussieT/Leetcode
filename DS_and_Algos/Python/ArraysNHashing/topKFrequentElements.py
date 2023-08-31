class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        my_hash = {}

        for val in nums:
            
            if val in my_hash:
                my_hash[val] += 1
            
            else:
                my_hash[val] = 1
        
        print("my hash : ", my_hash)

myClass = Solution()
myClass.topKFrequent([1, 2, 3, 3], 4)
