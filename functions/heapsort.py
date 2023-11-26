from heaps.max_heap import MaxHeap


def heapSort(passedList):
    mh = MaxHeap(len(passedList))
    for item in passedList:
        mh.insert(item)
    li = []
    print(mh.Heap)
    mh.maxHeapify(0)

    print(mh.Heap)
    while (it := mh.extractMax()) != None:
        li.append(it)
        mh.maxHeapify(0)
    print(li)
    passedList = li
    return li


def heapsort(data):
    for key in data:
        if type(data.get(key)) == list:
            tmp = data.get(key)
            print(tmp)
            heapSort(tmp)
