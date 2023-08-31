class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff < 0: return False # edge case 
        
        seen = {}
        
        for i, x in enumerate(nums): 
            if x < 0:
                bkt = (x * -1) // (indexDiff + 1)
            else:
                bkt = x//(indexDiff+1)

            if bkt in seen and i - seen[bkt][0] <= indexDiff:
                print(f"seen {seen} and {seen[bkt][0]}")

            if bkt-1 in seen and i - seen[bkt-1][0] <= indexDiff and abs(x - seen[bkt-1][1]) <= valueDiff:   
                print(abs(x - seen[bkt-1][1]) <= valueDiff)
   
            if bkt+1 in seen and i - seen[bkt+1][0] <= indexDiff and abs(x - seen[bkt+1][1]) <= indexDiff:
                print(abs(x - seen[bkt+1][1]))

            seen[bkt] = (i, x) 

        print("done")

        return False

myClass = Solution()
myClass.containsNearbyAlmostDuplicate([2,0,-2,2], 2, 1)
