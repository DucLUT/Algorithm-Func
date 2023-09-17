def karatsuba(x, y):
    # Base case: If either x or y is a single-digit number, use regular multiplication
    if x < 10 or y < 10:
        return x * y

    # Find the number of digits in the two numbers
    x_str = str(x)
    y_str = str(y)
    n = max(len(x_str), len(y_str))
    n_half = n // 2

    # Split the numbers into two halves
    a = x // 10**n_half
    b = x % 10**n_half
    c = y // 10**n_half
    d = y % 10**n_half

    # Recursive calls to compute the products and cross product
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    # Combine the results using the Karatsuba formula
    result = ac * 10**(2 * n_half) + ad_bc * 10**n_half + bd

    return result

# Example usage
x = 12345
y = 6789
result = karatsuba(x, y)
print(f"{x} * {y} = {result}")
