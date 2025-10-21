"""
Exemplo: Complexidade constante O(1)

Este script demonstra uma operação que é independente do tamanho da entrada:
- acesso por índice em uma lista (lista[0]) e uma operação aritmética simples.

Ele mede o tempo médio por operação para diferentes tamanhos de lista. Você verá
que o tempo por operação permanece (aproximadamente) constante quando n aumenta.
"""
from time import perf_counter
import random

def constant_operation(lst, trials=1000):
    # Acessa o primeiro elemento repetidamente — operação O(1)
    start = perf_counter()
    s = 0
    for _ in range(trials):
        x = lst[0]
        s += x + 1
    end = perf_counter()
    return (end - start) / trials

def main():
    sizes = [10**3, 10**4, 10**5]
    trials = 1000
    print("Demonstrando O(1): acesso por índice e operação aritmética")
    for n in sizes:
        lst = [random.randint(0, 100) for _ in range(n)]
        avg = constant_operation(lst, trials=trials)
        print(f"n={n:7d}  avg time/op = {avg*1e6:8.3f} µs")

if __name__ == '__main__':
    main()
