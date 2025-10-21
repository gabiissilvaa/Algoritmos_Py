from time import perf_counter
import random

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def avg_search_time(n, trials=1000):
    arr = list(range(n))
    start = perf_counter()
    for _ in range(trials):
        target = random.randint(0, n-1)
        _ = binary_search(arr, target)
    end = perf_counter()
    return (end - start) / trials

def main():
    sizes = [10**3, 10**4, 10**5]
    trials = 1000
    print("Demonstrando O(log n): busca binária em lista ordenada")
    for n in sizes:
        avg = avg_search_time(n, trials=trials)
        print(f"n={n:7d}  avg time/search = {avg*1e6:8.3f} µs")

if __name__ == '__main__':
    main()
