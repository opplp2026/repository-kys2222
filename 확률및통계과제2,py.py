import matplotlib.pyplot as plt

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def combination(n, r):
    result = factorial(n) // (factorial(r) * factorial(n - r))
    return result

def binomial(n, x, p):
    result = combination(n, x) * (p ** x) * ((1 - p) ** (n - x))
    return result
n_list = [20, 30, 40, 50]

p_list = [1/6, 2/6, 3/6]
for p in p_list:

    
    plt.figure(figsize=(9, 5))

    for n in n_list:
        x = list(range(n + 1))
        y = []

        for i in x:
            y.append(binomial(n, i, p))

        plt.plot(x, y, marker='o', markersize=3, label=f'n={n}')

    plt.title(f'Binomial Distribution (p={p:.3f})')
    plt.xlabel('Number of Successes (x)')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid()
    plt.show()