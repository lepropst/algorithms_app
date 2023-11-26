import importlib
from importlib import import_module

import json
import os
import sys


def main(data):
    file_name = sys.argv[1]

    # Verify that the file exists in the "functions" directory
    file_path = os.path.join("functions", f"{file_name}.py")
    file_path_python = f"functions.{file_name}"
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist in the 'functions' directory.")
        return

    mod = import_module(file_path_python)
    function = getattr(mod, file_name)

    print(function(data))

    return data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filename.py <file_name>")
        sys.exit(1)

    with open("data.json") as file:
        data = json.loads(file.read())

    # print(
    #     json.dumps(data.get("data_structure_nodes"), indent=2),
    #     data.get("numerical_arr"),
    #     data.get("lexical_arr"),
    #     sep="\n",
    # )
    tmp = main(data)
    if len(tmp) > 1:
        tmp = [{str(t): [str(x) for x in tmp[t]].__str__()} for t in tmp]
    print(json.dumps(tmp, indent=2))
