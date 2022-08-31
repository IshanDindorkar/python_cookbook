"""
Use of defaultdict
"""
from collections import defaultdict


def main():
    def_dict_as_list()

    def_dict_as_set()


def def_dict_as_list():
    def_dict = defaultdict(list)
    def_dict["a"].append(1)
    def_dict["a"].append(2)
    def_dict["b"].append(10)
    def_dict["c"].append(40)

    print(def_dict)


def def_dict_as_set():
    def_dict = defaultdict(set)
    def_dict["a"].add(1)
    def_dict["a"].add(1)  # will not add duplicate if set is used as implementation mode
    def_dict["b"].add(10)
    def_dict["c"].add(40)

    print(def_dict)


if __name__ == "__main__":
    main()


"""
Discussion: Why we need defaultdict?
To avoid writing code like this =>
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
"""