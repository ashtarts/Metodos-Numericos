import math

def f(x):
    return math.exp(-x)

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

def minimum_subintervals(a, b, epsilon):
    n = 1
    integral_value = trapezoidal_rule(a, b, n)
    prev_integral_value = integral_value + 2 * epsilon  # initialize with a value greater than epsilon
    while abs(integral_value - prev_integral_value) > epsilon:
        n += 1
        prev_integral_value = integral_value
        integral_value = trapezoidal_rule(a, b, n)
    return n


a = 1
b = 2
n_4 = 4
n_6 = 6

integral_value_4 = trapezoidal_rule(a, b, n_4)
integral_value_6 = trapezoidal_rule(a, b, n_6)
print("Integral using 4 divisions:", integral_value_4)
print("Integral using 6 divisions:", integral_value_6)

epsilon = 1e-5
min_subintervals = minimum_subintervals(a, b, epsilon)
print("Minimum subintervals to reach precision of", epsilon, ":", min_subintervals)
