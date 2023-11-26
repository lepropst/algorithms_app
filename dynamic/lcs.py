import itertools
import numpy as np


def lcs(X, Y):
    m = len(X)

    n = len(Y)

    table = [[0] * (n + 1) for i in range(m + 1)]
    lexical_table = [[""] * (n + 1) for i in range(m + 1)]
    paths = []
    lexical_table_reprs = []
    table_reprs = []
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 0 or j == 0:
                table[i][j] = ""
                lexical_table[i][j] = ""
            elif X[i - 1] == Y[j - 1]:
                lexical_table[i][j] = f"{lexical_table[i - 1][j - 1]}{X[i - 1]}"
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = table[i][j - 1]

                if table[i - 1][j] >= table[i][j - 1]:
                    table[i][j] = table[i - 1][j]
                    lexical_table[i][j] = lexical_table[i - 1][j]
                    tmp = f"{X[i-1]} {Y[j-1]}\n"
                    tmp1 = np.array(table)

                    if (tmp1 == 0).all():
                        s = ["EMPTY TABLE"]
                    else:
                        s = [[e for e in row] for row in table]

                    ls = [str(row) for row in lexical_table]
                    table_reprs.append(s)
                    lexical_table_reprs.append("\n".join(ls))
                else:
                    table[i][j] = table[i][j - 1]
                    lexical_table[i][j] = lexical_table[i][j - 1]
                    tmp = f"({i-1}, {j})"
                    tmp1 = np.array(table)

                    if (tmp1 == 0).all():
                        s = ["EMPTY TABLE"]
                    else:
                        s = [[e for e in row] for row in table]

                    ls = [str(row) for row in lexical_table]
                    table_reprs.append(s)
                    lexical_table_reprs.append("\n".join(ls))
            # paths.append(f"path:{tmp}\n")

    print(
        f"The following format is how I copied and filled in my tables:\n\n```\n\t[chosen value from table]\t[path taken]\n\n\t[Table Representation]\n```\n"
    )
    column_labels = list(Y)
    row_labels = list(X)
    print(f"LONGESET LEXICAL PATTERN {lexical_table[m][n]}")
    for l in ["-", "-", *column_labels]:
        print(l, end="      ")
    print()
    for ind, row in enumerate(table_reprs[len(table_reprs) - 1]):
        tmp = ""
        if ind == 0:
            print("-", end="")
        if row_labels[ind - 1] != None and ind > 0:
            tmp = f"{row_labels[ind-1]}"
        print(tmp, end="      ")
        for i in row:
            print(i, end="      ")
        print("\n")

    return {"numerical_result": table[m][n], "lex_result": lexical_table[m][n]}


# end of function lc
