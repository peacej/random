def sqrt_halving(x, epsilon=0.0001):
    if x <= 1:
        res = x + (1 - x) / 2
    elif x > 1:
        res = 1 + (x - 1) / 2
    else:
        raise ValueError("invalid input")
    if res * res < x:
        while res * res < x:
            prev_delta = res
            res = 2 * res
    else:
        while res * res > x:
            prev_delta = res
            res = res / 2
    while abs(res * res - x) > epsilon:
        if res * res > x:
            res = res - prev_delta / 2
        else:
            res = res + prev_delta / 2
        prev_delta = prev_delta / 2
    return res

def sqrt_newton(x, epsilon=0.0001):
    if x <= 1:
        res = x + (1 - x) / 2
    elif x > 1:
        res = 1 + (x - 1) / 2
    else:
        raise ValueError("invalid input")
    while abs(res * res - x) > epsilon:
        res = (x + res*res) / (2 * res) # manually did algebra using newton's method
    return res

print(sqrt_halving(.05))
print(sqrt_newton(.05))
print(sqrt_halving(1.5))
print(sqrt_newton(1.5))
print(sqrt_halving(53))
print(sqrt_newton(53))


