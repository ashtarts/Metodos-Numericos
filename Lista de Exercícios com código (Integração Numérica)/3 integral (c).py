import math

def f(x):
    return 1 / math.sqrt(x)

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
    p_i = i + 2 * epsilon
    while abs(i - p_i) > epsilon:
        n += 1
        p_i = i
        i = t(a, b, n)
    return n


a = 2
b = 5
n_4 = 4
n_6 = 6

i4 = t(a, b, n_4)
i6 = t(a, b, n_6)

print("4", i4)
print("6", i6)

epsilon = 1e-5

min = m(a, b, epsilon)
print(min)

integral = t(a, b, min)
print(integral)
