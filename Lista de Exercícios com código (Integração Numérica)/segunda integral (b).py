import math

def f(x):
    return math.sqrt(x)

def t(a, b, n):
    h = (b - a) / n
    r = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        r += f(a + i * h)
    r *= h
    return r

def m(a, b, epsilon):
    n = 1
    i = t(a, b, n)
    piv = i + 2 * epsilon
    while abs(i - piv) > epsilon:
        n += 1
        piv = i
        i = t(a, b, n)
    return n

a = 1
b = 4
e = 1e-5
min = m(a, b, e)
print(min)

integral = t(a, b, min)
print(integral)
