from dynamic.lcs import lcs


def dynamic_lcs(data):
    string_one = data.get("string_one")
    string_two = data.get("string_two")
    return lcs(string_one, string_two)
