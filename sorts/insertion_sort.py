def insertionSort(b, comparator=lambda x, y: x > y):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and comparator(b[j], up):
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up

    return b
