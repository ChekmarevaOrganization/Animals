def factorial(x):
    if x < 0:
        raise ValueError('x must be >= 0')
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result