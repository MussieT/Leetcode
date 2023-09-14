def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursive calls to divide the array further
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    print(f"left is {left} and right is {right}")
    # Merge the two sorted subarrays
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Append the remaining elements, if any
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    # print(f"merged: {merged}")
    
    return merged

# Example usage
arr = [4, 2, 6, 3, 7, 5, 8, 1]
sorted_arr = merge_sort(arr)
print(sorted_arr)
