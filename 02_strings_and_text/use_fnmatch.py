# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Use of fnmatch and fnmatchcase functions to do text searching/pattern matching
"""
from fnmatch import fnmatch, fnmatchcase
from typing import List


def main():
    # 1. create dummy list of few addresses
    address_list = create_address_list()

    # 2. filter addresses that match a specific pattern
    pattern = r"1[0-9][0-9][0-9] * ST"
    filtered_address_list = filter_addresses(address_list=address_list, pattern=pattern, match_case=False)
    print(f"Filtered address list: {filtered_address_list}")


def create_address_list():
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]

    return addresses


def filter_addresses(address_list: List, pattern: str, match_case=True):
    if match_case:
        return [address for address in address_list if fnmatch(address, pattern)]
    else:
        return [address for address in address_list if fnmatchcase(address, pattern)]


if __name__ == "__main__":
    main()


"""
Discussion:
fnmatch() and fnmatchcase() provides search functionality that sits between simple string matching
and full blown power of using regular expressions 
"""