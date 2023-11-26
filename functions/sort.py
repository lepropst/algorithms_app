from sorts.bubble_sort import BubbleSort
from sorts.heapSort import heapSort
from sorts.insertion_sort import insertionSort
from sorts.mergeSort import mergeSort
from sorts.quickSort import quickSort
from sorts.shell_sort import shellSort


def sort(data):
    # numerical_arr = data.get("numerical_arr")
    # lexical_arr = data.get("lexical_arr")
    # print(insertionSort(numerical_arr))
    # print(insertionSort(lexical_arr))
    # numerical_arr = data.get("numerical_arr")
    # lexical_arr = data.get("lexical_arr")
    # print(BubbleSort(numerical_arr))
    # print(BubbleSort(lexical_arr))
    # numerical_arr = data.get("numerical_arr")
    # lexical_arr = data.get("lexical_arr")
    # print(shellSort(numerical_arr))
    # print(shellSort(lexical_arr))
    # numerical_arr = data.get("numerical_arr")
    # lexical_arr = data.get("lexical_arr")

    # print(numerical_arr)
    # print(lexical_arr)
    # numerical_arr = data.get("numerical_arr")
    # lexical_arr = data.get("lexical_arr")
    # quickSort(0, len(numerical_arr) - 1, numerical_arr)
    # print(numerical_arr)
    # quickSort(0, len(lexical_arr) - 1, lexical_arr)
    # print(lexical_arr)
    numerical_arr = data.get("numerical_arr")
    lexical_arr = data.get("lexical_arr")
    heapSort(numerical_arr)
    heapSort(lexical_arr)
    print(numerical_arr)
    print(lexical_arr)
