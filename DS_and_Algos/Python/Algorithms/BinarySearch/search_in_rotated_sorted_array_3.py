def search_target_in_rotated_array(nums: list[int], target: int) -> int:
        n = len(nums) - 1
        left, right = 0, n

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            elif nums[right] == nums[mid] and nums[left] == nums[mid]:
                right -= 1
                left += 1
            
            elif nums[left] <= nums[mid]:

                if target < nums[mid] and target >= nums[left]:
                    print("first")
                    right = mid - 1
                
                else:
                    print("second")
                    left = mid + 1

            else:

                if target <= nums[right] and target > nums[mid]:
                    print("third")
                    left = mid + 1
                
                else:
                    print("fourth")
                    right = mid - 1
        
        return False

print(search_target_in_rotated_array([3, 1], 1))
