#3. Skapa en Fibonacci-sekvensgenerator.

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Generera det 10:e Fibonacci-talet
print(fibonacci_recursive(7))  # Output: 55

###################################################################

def fibonacci_loop(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generera de första 10 Fibonacci-talen
print(list(fibonacci_loop(10)))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
