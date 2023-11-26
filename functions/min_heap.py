from heaps.max_heap import MaxHeap, create_max_heap
from heaps.min_heap import insert_min_heap


def min_heap(data):
    mh = []
    maxh = MaxHeap(len(data.get("numerical_arr")))
    for x in data.get("numerical_arr"):
        insert_min_heap(mh, x)
        maxh.insert(x)
    print(mh)
    try:
        while h := mh.pop():
            print(h)
    except IndexError:
        print("max heeap")
        maxh.Print()
