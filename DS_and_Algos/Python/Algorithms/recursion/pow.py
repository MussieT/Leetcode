# tricky part - divide and conquer - 2^10 meaning 2^5 * 2^5
def pow(x: float, n: int) -> float:
    
    if n == 1 or n == -1:
        return x
    
    if n < 0:
        return 1 / (x * pow(x, n + 1))

    return x * pow(x, n - 1)

print(pow(2.0000, -2))
