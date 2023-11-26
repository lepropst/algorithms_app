from sorts.insertion_sort import insertionSort


def binSort(arr: list[int]):
    MAXIMUM = max(arr) + 1
    sortedBins = [[]] * MAXIMUM
    for item in arr:
        if sortedBins[item]:
            sortedBins[item].append(item)
        else:
            sortedBins[item] = [item]

    arr.clear()

    for local_list in sortedBins:
        arr.extend(local_list)
    return arr


def binSortLexical(arr: list[str]):
    MAX = max([ord(x) for x in arr]) + 1
    sortedBins = [[]] * MAX
    for item in arr:
        sortedBins[ord(item)] = item
    arr.clear()
    for local_list in sortedBins:
        arr.extend(local_list)

    return arr
