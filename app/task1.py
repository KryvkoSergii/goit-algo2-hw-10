import random
import timeit
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def print_results(timings):
    for n, (rand, determ) in timings.items():
        print(f"Number of elements: {n}")
        print(f"\t Randomized QuickSort: {rand:4f} sec")
        print(f"\t Deterministic QuickSort: {determ:4f} sec")
        print()

def draw_graph(timings):
    numbers = list(timings.keys())
    rand_results = [x[0] for x in timings.values()]
    determ_results = [x[1] for x in timings.values()]
    plt.plot(numbers,rand_results,"-o",label="Randomized QuickSort",)
    plt.plot(numbers, determ_results, "-o", label="Deterministic QuickSort")
    plt.xlabel("Array size (n)")
    plt.ylabel("Average time (seconds)")
    plt.title("Randomized and Deterministic QuickSort performance comparison")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()

elemets_number = [10_000, 50_000, 100_000, 500_000]
timings = {}
for n in elemets_number:
    arr = [random.randint(0, 1000) for _ in range(n)]
    rand = timeit.timeit(lambda: randomized_quick_sort(arr), number=5)
    determ = timeit.timeit(lambda: deterministic_quick_sort(arr), number=5)
    timings[n] = (rand, determ)
    print(f"Finished for array size {n}")

print_results(timings)
draw_graph(timings)


