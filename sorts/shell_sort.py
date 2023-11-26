# Set initial gap (see next section)
# Loop1 while (gap > 1)
# Reduce gap (see next section)
# index = gap
# Loop2 while (index < listSize)
# insertValue = List[index]
# tryIdx = index - gap
# Loop3 while ((tryIdx >= 0) AND (insertValue < list[tryIdx]))
# List [tryIdx + gap] = List [tryIdx]
# tryIdx = tryIdx – gap
# List [tryIdx + gap] = insertValue
# Increment index


def shellSort(arr: list):
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            insertValue = arr[i]
            j = i
            while j >= gap and arr[j - gap] > insertValue:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = insertValue

        gap = gap // 2
    return arr
