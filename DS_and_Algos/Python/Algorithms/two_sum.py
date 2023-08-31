class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        left, right = 0, len(numbers) - 1
        for index, element in enumerate(numbers):

            while left <= right:

                mid = (left + right) // 2
                sum = numbers[mid] + element

                print("sum is: ", sum)
                print("index is: ", index)

                if sum == target and index != mid:
                    print("here we are : ", index, " and ", mid)
                    return [index, mid]
                            
                elif sum < target:
                    left = mid + 1
                
                else:
                    right = mid - 1


new_solution = Solution()
new_solution.twoSum([2,7,11,15], 9)
