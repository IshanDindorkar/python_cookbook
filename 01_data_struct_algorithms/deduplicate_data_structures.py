# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Remove duplicate items from list, dictionary etc.
"""
from typing import List


def main():
    pass

    # 1. create list of some elements having duplicates
    num_list = [1, 3, 5, 3, 7, 4, 9, 8, 4]

    # 2. remove duplicates from the above list
    print(list(remove_duplicates_from_list(num_list=num_list)))

    # 3. create list of duplicate dictionaries
    duplicate_dicts = [
        {"x": 1, "y": 2},
        {"x": 3, "y": 4},
        {"x": 1, "y": 2},
        {"x": 5, "y": 6},
        {"x": 7, "y": 8},
        {"x": 3, "y": 4},
        {"x": 9, "y": 10},
    ]

    # 4. remove duplicate dictionaries from above list
    print(list(remove_dup_dicts_from_list(dict_list=duplicate_dicts,
                                          key=lambda dictionary: (dictionary["x"], dictionary["y"]))))


def remove_duplicates_from_list(num_list: List):
    seen_nums = list()
    for num in num_list:
        if num not in seen_nums:
            yield num
            seen_nums.append(num)


def remove_dup_dicts_from_list(dict_list: List, key=None):
    seen_dict = set()
    for dictionary in dict_list:
        if key is None:
            seen_dict.add(dictionary)
        else:
            if key(dictionary) not in seen_dict:
                yield dictionary
                seen_dict.add(key(dictionary))


if __name__ == "__main__":
    main()
