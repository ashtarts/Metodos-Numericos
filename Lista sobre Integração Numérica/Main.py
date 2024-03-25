import math

def fa(x):
    return 1 / math.cos(x)

def trapezoidal_rule_a(a, b, n):
    h = (b - a) / n
    sum_val = 0.5 * (fa(a) + fa(b))
    for i in range(1, n):
        x = a + i * h
        sum_val += fa(x)
    return h * sum_val

def fb(x):
    return 4 / (2 + math.pow(x, 4))

def trapezoidal_rule_b(a, b, n):
    h = (b - a) / n
    sum_val = 0.5 * (fb(a) + fb(b))
    for i in range(1, n):
        x = a + i * h
        sum_val += fb(x)
    return h * sum_val

def fc(x):
    return 2 / math.sqrt(1 + math.pow(x, 2))

def trapezoidal_rule_c(a, b, n):
    h = (b - a) / n
    sum_val = 0.5 * (fc(a) + fc(b))
    for i in range(1, n):
        x = a + i * h
        sum_val += fc(x)
    return h * sum_val

def fd(x):
    return math.pow(math.cos(x), 3)

def trapezoidal_rule_d(a, b, n):
    h = (b - a) / n
    sum_val = 0.5 * (fd(a) + fd(b))
    for i in range(1, n):
        x = a + i * h
        sum_val += fd(x)
    return h * sum_val

def fa2(x):
    return -1 / math.cos(x) + 2 * (1 / math.pow(math.cos(x), 3))

def error_a(b, a, n):
    aux = fa2(b)
    h = (b - a) / n
    aux = (aux * n * (math.pow(h, 3))) / 12
    return aux

def fb2(x):
    return (-(16 * math.pow(x, 2) * (-5 * math.pow(x, 4) + 6))) / math.pow(2 + math.pow(x, 4), 3)

def error_b(b, a, n):
    aux = fb2(b)
    h = (b - a) / n
    aux = (aux * n * (math.pow(h, 3))) / 12
    return aux

def fc2(x):
    return (-(2 * (-2 * math.pow(x, 2) + 1))) / (math.pow(1 + math.pow(x, 2), 2.5))

def error_c(b, a, n):
    aux = fc2(b)
    h = (b - a) / n
    aux = (aux * n * (math.pow(h, 3))) / 12
    return aux

def fd2(x):
    return -3 * (-2 * math.cos(x) + 3 * math.pow(math.cos(x), 3))

def error_d(b, a, n):
    aux = fd2(b)
    h = (b - a) / n
    aux = (aux * n * (math.pow(h, 3))) / 12
    return aux

if __name__ == "__main__":
    a = 0
    a2 = -4
    a3 = -4
    a4 = 0

    b = math.pi / 4
    b2 = 4
    b3 = 4
    b4 = math.pi / 2

    result = 0
    result2 = 0
    result3 = 0
    result4 = 0

    result = trapezoidal_rule_a(a, b, 3)
    result2 = trapezoidal_rule_b(a2, b2, 9)
    result3 = trapezoidal_rule_c(a3, b3, 8)
    result4 = trapezoidal_rule_d(a4, b4, 4)

    print("Questões normais")
    print(" ")
    print("Questão 1:", result)
    print("Questão 2:", result2)
    print("Questão 3:", result3)
    print("Questão 4:", result4)
    print(" ")

    result_a1 = 0
    result_a2 = 0
    result_a3 = 0
    result_a4 = 0

    result_a1 = error_a(b, a, 3)
    result_a2 = error_b(b2, a2, 9)
    result_a3 = error_c(b3, a3, 8)
    result_a4 = error_d(b4, a4, 4)

    print("Questão com o erro")
    print(" ")
    print("Questão 1:", result_a1)
    print("Questão 2:", result_a2)
    print("Questão 3:", result_a3)
    print("Questão 4:", result_a4)

    print(" ")
    print("Questão de comparação de erros: ")
    print("Comparação 1:", (result - result_a1))
    print("Comparação 2:", (result2 - result_a2))
    print("Comparação 3:", (result3 - result_a3))
    print("Comparação 4:", (result4 - result_a4))
