def PE97(a, b, c, m):
    return (c * pow(a, b, m) + 1) % m

f  =PE97(2, 7830457, 28433, 10**10)
print(f)