# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Use of ChainMap to merge two dictionaries
"""
from collections import ChainMap


def main():
    a_dict = {
        "x": 1,
        "z": 2
    }

    b_dict = {
        "y": 3,
        "z": 8
    }

    merged_a_b_dict = ChainMap(a_dict, b_dict)
    print(merged_a_b_dict["z"])


if __name__ == "__main__":
    main()


"""
Discussion:
An alternative to ChainMap is to use "update" function provided by dictionary.
The "update" function will create a new dictionary by fusing together two dictionaries.
It creates problem if any one of the original dictionary is updated. In that case, the
change is not reflected in the merged dictionary. But that is not the case with ChainMap.
A ChainMap is using original dictionaries.

A typical usecase for ChainMap is when we have to lookup a key in first dictionary and if it is not
found we do a lookup in the other dictionary. A ChainMap fuses two dictionaries so that lookups can be
avoided.
"""