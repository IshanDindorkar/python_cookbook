# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Group records based on criteria(attribute/field value)
NOTE: first sort, the group using same key
"""
from itertools import groupby
from operator import itemgetter
from typing import List


def main():
    # 1. create list of dictionaries having "date" as one of the key
    dict_list = create_dict_list()

    # 2. sort list based on date
    sorted_dict_list = sort_dict_list(dict_list=dict_list)
    print(f"Sorted based on date: {sorted_dict_list}")

    # 3. group by date and print out dictionaries
    group_by_date(dict_list=sorted_dict_list)


def create_dict_list():
    dict_list = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    return dict_list


def sort_dict_list(dict_list: List):
    # Lambda function will return value for date key for every dictionary and it will be used for sorting
    return sorted(dict_list, key=lambda d: d["date"])


def group_by_date(dict_list: List):
    # for date, items in groupby(dict_list, key=itemgetter("date")):
    for date, items in groupby(dict_list, key=lambda d: d["date"]):
        print(date)
        for idx, item in enumerate(items):
            print(f"          {idx+1}. {item}")


if __name__ == "__main__":
    main()
