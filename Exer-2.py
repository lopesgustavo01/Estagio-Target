def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n or n == 0:
        return True
    else:
        return False

numero = int(input("Informe um número: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
