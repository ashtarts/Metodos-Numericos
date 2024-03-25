import math

def f(x):
    return math.sqrt(x)

def sla(a, b, n):
    h = (b - a) / n
    r = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        r += f(a + i * h)
    r *= h
    return r

def m(a, b, epsilon):
    n = 1
    i = sla(a, b, n)
    p_i = i + 2 * epsilon
    while abs(i - p_i) > epsilon:
        n += 1
        p_i = i
        i = sla(a, b, n)
    return n


a = 1
b = 4  # Limite superior alterado para 4
epsilon = 1e-5

min = m(a, b, epsilon)
print("Minimum subintervals to reach precision of", epsilon, ":", min)

integral = sla(a, b, min)
print("Integral of √x from", a, "to", b, ":", integral)
