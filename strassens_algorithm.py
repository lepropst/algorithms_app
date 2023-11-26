import numpy as np


def split(matrix):
    """
    Splits a given matrix into quarters.
    Input: nxn matrix
    Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
    """
    row, col = np.shape(matrix)
    row2, col2 = row // 2, col // 2
    return (
        matrix[:row2, :col2],
        matrix[:row2, col2:],
        matrix[row2:, :col2],
        matrix[row2:, col2:],
    )


def pretty_print(m):
    s = [[str(e) for e in row] for row in m]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "\t".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    for row in table:
        print(row)
    print("-------------------")


def strassen(x: np.array, y: np.array):
    """
    Computes matrix product by divide and conquer approach, recursively.
    Input: nxn matrices x and y
    Output: nxn matrix, product of x and y
    """

    # Base case when size of matrices is 1x1
    if len(x) == 1:
        # print(f"Base case of matrix {x} and {y} reached. Recursivly returns {x*y}")
        return x * y

    # Splitting the matrices into quadrants. This will be done recursively
    # until the base case is reached.

    a00, a01, a10, a11 = split(x)
    b00, b01, b10, b11 = split(y)
    parts = [
        ("a00 of A", a00),
        ("a01 of A", a01),
        ("a10 of A", a10),
        ("a11 of A", a11),
        ("b00 of B", b00),
        ("b01 of B", b01),
        ("b10 of B", b10),
        ("b11 of B", b11),
    ]
    for part in parts:
        print(f"{part[0]}, {part[1]}", sep="\n")
    # Computing the 7 products, recursively (m1, m2...m7)
    m1 = strassen(a00, b01 - b11)
    m2 = strassen(a00 + a01, b11)
    m3 = strassen(a10 + a11, b01)
    m4 = strassen(a11, b10 - b00)
    m5 = strassen(a00 + a11, b00 + b11)
    m6 = strassen(a01 - a11, b10 + b11)
    m7 = strassen(a00 - a10, b00 + b01)
    products = [
        (f"M1 = A00 x (B01 - B11)\t= {m1[0]}"),
        (f"M2 = (A00 + A01) x B11\t= {m2[0]}"),
        (f"M3 = (A10 + A11) x B00\t= {m3[0]}"),
        (f"M4 = A11 x (B10 - B00)\t= {m4[0]}"),
        (f"M5 = (A00 + A11)(B00 + B11)\t= {m5[0]}"),
        (f"M6 = (A01 - A11) x (B10 + B11)\t= {m6[0]}"),
        (f"M7 = (A00 - A10) x (B00 + B01)\t= {m7[0]}"),
    ]

    for product in products:
        print(product)

    # Computing the values of the 4 quadrants of the final matrix c
    c11 = m5 + m4 - m2 + m6
    c12 = m1 + m2
    c21 = m3 + m4
    c22 = m1 + m5 - m3 - m7

    tmp = [f"C00 = M5 + M6 + M4 - M2 = {c11[0]}"]
    tmp1 = [f"C01 = M1 + M2 = {c12[0]}"]
    tmp2 = [f"C10 = M3 + M4 = {c21[0]}"]
    tmp3 = [f"C11 = M1 - M7 - M3 + M5 = {c22[0]}"]
    print(tmp)
    print(tmp1)
    print(tmp2)
    print(tmp3)

    # print("Quadrants:\n", tmp, tmp1, tmp2, tmp3)

    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    h1 = np.hstack((c11, c12))
    h2 = np.hstack((c21, c22))

    c = np.vstack(((h1), (h2)))
    # c = np.array([[c11, c12], [c21, c22]])
    return c


# Divide:
# Partition A and B into n/2-by-n/2 blocks
# Partition A Partition B
# Calculate:
# Multiply seven n/2-by-n/2 matrices recursively
# M1 = A00 x (B01 - B11)
# M2 = (A00 + A01) x B11
# M3 = (A10 + A11) x B00
# M4 = A11 x (B10 - B00)
# M5 = (A00 + A11)(B00 + B11)
# M6 = (A01 - A11) x (B10 + B11)
# M7 = (A00 - A10) x (B00 + B01)

# Conquer:
# Combine the seven products into 4 terms using 8 matrix additions/subtractions
# C00 = M5 + M6 + M4 - M2
# C01 = M1 + M2
# C10 = M3 + M4
# C11 = M1 - M7 - M3 + M5
