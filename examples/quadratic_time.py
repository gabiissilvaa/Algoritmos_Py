"""
Exemplo: Complexidade quadrática O(n^2)

Este script demonstra um algoritmo de comparação todos-contra-todos (laços
aninhados) que conta pares com soma igual a um valor alvo. Mede tempos para
vários tamanhos de entrada para ilustrar crescimento quadrático.
"""
from time import perf_counter
import random

def count_pairs_bruteforce(arr, target):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count

def avg_time(n, trials=10):
    # usar menos trials pois O(n^2) cresce rápido
    arr = [random.randint(0, 1000) for _ in range(n)]
    start = perf_counter()
    for _ in range(trials):
        _ = count_pairs_bruteforce(arr, target=100)
    end = perf_counter()
    return (end - start) / trials

def main():
    sizes = [100, 200, 400]
    trials = 5
    print("Demonstrando O(n^2): laços aninhados contando pares")
    for n in sizes:
        avg = avg_time(n, trials=trials)
        print(f"n={n:4d}  avg time/run = {avg:.6f} s")

if __name__ == '__main__':
    main()
