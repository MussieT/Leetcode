def find_rotated_index(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return left

print("find rotated: ", find_rotated_index([4, 5, 6, 7, 8, 1, 2]))