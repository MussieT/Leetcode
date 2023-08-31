import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # finding minimum bananas-per-hour k
        # every element spends unknown hour hr, since koko cannot go to another pile -> use math.ceil if 4 banans per hour, for 5 banana 2 hrs..
        # the math, math.ceil (element/k), minimum, 1, maximum will be given total hours

        left, right, res = 1, max(piles), max(piles)

        while left <= right:

            mid = (left + right) // 2

            sum = 0
            for num in piles:
               sum += (math.ceil(num / mid))

            if sum <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res

ExampleSolution = Solution()
print(ExampleSolution.minEatingSpeed([30,11,23,4,20], 6))