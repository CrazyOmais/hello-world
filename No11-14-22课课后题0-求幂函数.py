def power(x, y):
    n = y - 1
    result = x
    if n:
        result *= power(result, n)
    return result

print(power(2, 10))
