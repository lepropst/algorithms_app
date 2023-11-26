from dynamic.knapsack_01 import knapsack


def dynamic_knapsack(data):
    arr = data.get("knapsack_arr")
    wts = [x.get("weight") for x in arr]
    val = [x.get("profit") for x in arr]
    MAX = 14
    kn = knapsack(wts, val, MAX, len(val))
    print(kn)
