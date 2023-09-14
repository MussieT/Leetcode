class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        max_avg = window / k
        
        for i in range(k, len(nums)):
            window += nums[i]
            window -= nums[i - k]
            
            current_avg = window / k
            print(f"current avg {current_avg} and max_avg {max_avg}")
            max_avg = max(max_avg, current_avg)
           
        return max_avg

mySolution = Solution()
print(mySolution.findMaxAverage([0,4,0,3,2], 1))
