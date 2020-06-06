def sqrt_halving(x, epsilon=0.0001):
    if x > 0:
        res = (x + 1) / 2
    else:
        raise ValueError("invalid input")
    i = 0
    if res * res < x:
        while res * res < x:
            prev_delta = res
            res = 2 * res
            i +=1
    else:
        while res * res > x:
            prev_delta = res
            res = res / 2
            i +=1
    while abs(res * res - x) > epsilon:
        if res * res > x:
            res = res - prev_delta / 2
        else:
            res = res + prev_delta / 2
        prev_delta = prev_delta / 2
        i += 1
    print(f"Took {i} iterations to find solution.")
    return res

def sqrt_newton(x, epsilon=0.0001):
    if x > 0:
        res = (x + 1) / 2
    else:
        raise ValueError("invalid input")
    i = 0
    while abs(res * res - x) > epsilon:
        res = (x + res*res) / (2 * res) # manually did algebra using newton's method
        i += 1
    print(f"Took {i} iterations to find solution.")
    return res

for value in [0.05, 1.5, 53, 4450455]:
    print(f"Calculating square root for {value}...")
    print(sqrt_halving(value))
    print(sqrt_newton(value))
