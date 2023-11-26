def insert_min_heap(heap: list, value):
    # Add the new element to the end of the heap
    heap.append(value)
    # Get the index of the last element
    index = len(heap) - 1
    # Compare the new element with its parent and swap if necessary
    while index > 0 and heap[(index - 1) // 2] > heap[index]:
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]

        # Move up the tree to the parent of the current element
        index = (index - 1) // 2


def create_min_heap(arr: list):
    l = []
    for a in arr:
        insert_min_heap(l, a)
    return l
