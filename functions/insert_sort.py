import json

from sorts.insertion_sort import insertionSort


def insert_sort(data):
    numerical_arr, lexical_arr, data_structure_nodes = data
    if len(data.get(numerical_arr)) > 2:
        insertionSort(data.get("numerical_arr"))
    if len(data.get(lexical_arr)) > 2:
        insertionSort(data.get("lexical_arr"))
    if len(data.get(data_structure_nodes)) > 2:
        insertionSort(data.get("data_structure_nodes"))
    return data
