"""
Unpack different types of iterables like tuple, list etc.
"""
from typing import List


def main():
    num_seq = (4, 5)
    x, y = unpack_numbers(seq=num_seq)
    print(f"Printing sequence of numbers => {x} | {y}")

    nested_seq = ["ACME", 50, 91.1, (2012, 12, 21)]
    name, shares, price, year, month, date = unpack_nested_seq(seq=nested_seq)
    print(f"Printing elements of nested seq: {name} | {shares} | {price} | {year} | {month} | {date}")

    variable_no_of_elements = ["Ishan Dindorkar", "ishan.dindorkar@yahoo.com", "123456", "456789"]
    name, email, phone_numbers = unpack_variable_elems(seq=variable_no_of_elements)
    print(f"Printing variable no of elements: {name} | {email} | {phone_numbers}")


def unpack_numbers(seq: tuple):
    x, y = seq
    return x, y


def unpack_nested_seq(seq: List):
    name, shares, price, (year, month, date) = seq
    return name, shares, price, year, month, date


def unpack_variable_elems(seq: List):
    name, email, *phone_numbers = seq
    return name, email, phone_numbers


if __name__ == "__main__":
    main()
