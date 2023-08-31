# Easy
def valid_perfect_square(num: int):
    left = 0
    right = num

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == num:
            return True
        elif mid * mid > num:
            right = mid - 1
        else:
            left = mid + 1
    return False

print(valid_perfect_square(100))