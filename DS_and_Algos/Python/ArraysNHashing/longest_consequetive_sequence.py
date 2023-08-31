class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # check if there is no element left (starting)
            if (num - 1) not in num_set:
                length = 1

                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)

        print(longest)

myClass = Solution()
myClass.longestConsecutive([12, 3, 4, 5, 1])
