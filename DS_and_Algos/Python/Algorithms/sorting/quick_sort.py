# This example includes additional space

def quickSort(arr: list):

    if len(arr) < 2:
        return arr
    
    pivot =  arr[-1]
    left_sub_array = []
    right_sub_array = []

    for i in range(len(arr) - 1):

        if arr[i] < pivot:
            left_sub_array.append(arr[i])
        else:
            right_sub_array.append(arr[i])

    return quickSort([x for x in arr if x < pivot]) + [pivot] + quickSort(right_sub_array)

print(quickSort([2, 1, 4, 3, 0, 0, 0, 5, 8]))
