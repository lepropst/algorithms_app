def BubbleSort(arr: list):
    listSorted = False
    while not listSorted:
        listSorted = True
        index = 0
        while index < len(arr) - 1:
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                listSorted = False
            index += 1
        index -= 1
    return arr
