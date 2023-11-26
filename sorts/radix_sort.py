from sorts.counting_sort import countingSort


def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        print(f"Counting sort with {exp}")
        countingSort(arr, exp)
        exp *= 10
    print(f"array: {arr}")
