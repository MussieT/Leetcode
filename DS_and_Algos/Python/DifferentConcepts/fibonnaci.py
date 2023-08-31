def fibonacci(n):
    a, b = 0, 1

    if n == 0:
        return n

    for i in range(2, n):
        print(f"i is {i}")
        c = a + b
        a = b
        b = c

    return b

print(fibonacci(10))
