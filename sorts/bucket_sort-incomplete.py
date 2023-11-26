from sorts.insertion_sort import insertionSort


def bucketSort(arr: list, buckets=10) -> list:
    sorted_list = [[]] * buckets

    # Put array elements in different buckets
    for item in arr:
        index = int(item / buckets)
        if index in sorted_list:
            sorted_list[index].append(item)
        else:
            sorted_list[index] = [item]

    for bucket in sorted_list:
        insertionSort(bucket)

    for i in range(0, buckets):
        arr.extend(sorted_list[i])

    return arr
