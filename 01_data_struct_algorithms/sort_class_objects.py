# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Sort objects of custom class using lambda function and also using attrgetter function provided by operator class
"""
from operator import attrgetter
from typing import List


class User:
    def __init__(self, uid: int, uname: str):
        self.uid = uid
        self.uname = uname

    def __repr__(self):
        return f"User id: {self.uid} | name: {self.uname}"


def main():
    users = create_user_list()

    sorted_obj_list_by_id = sort_objects_using_attrgetter(user_list=users, id=True)
    sorted_obj_list_by_name = sort_objects_using_attrgetter(user_list=users, id=False)

    print(f"Original object list: {users}")
    print(f"Sorted object list by id: {sorted_obj_list_by_id}")
    print(f"Sorted object list by name: {sorted_obj_list_by_name}")


def create_user_list():
    u1 = User(1, "A")
    u2 = User(4, "B")
    u3 = User(2, "C")
    u4 = User(3, "D")
    u5 = User(5, "E")
    users = [u1, u2, u3, u4, u5]

    return users


def sort_objects_using_lambda(user_list: List, id: bool):
    if id:
        return sorted(user_list, key=lambda u: u.uid)
    else:
        return sorted(user_list, key=lambda u: u.uname)


def sort_objects_using_attrgetter(user_list: List, id: bool):
    if id:
        return sorted(user_list, key=attrgetter("uid"))
    else:
        return sorted(user_list, key=attrgetter("uname"))


if __name__ == "__main__":
    main()
