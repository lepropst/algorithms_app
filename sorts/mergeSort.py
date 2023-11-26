def merge(arr: list, low, mid, high):
    n1 = (mid - low) + 1
    n2 = high - mid
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[low + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
    i, j = 0, 0
    k = low
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    return arr


def mergeSort(arr: list, low, high) -> list:
    if low < high:
        m = low + (high - low) // 2

        # Sort first and second halves
        mergeSort(arr, low, m)
        mergeSort(arr, m + 1, high)
        merge(arr, low, m, high)
