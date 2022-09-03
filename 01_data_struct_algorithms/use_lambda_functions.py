# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Practice use of lambda expressions
"""
from typing import List


def main():
    a = [
        {"x": 1, "y": 2},
        {"x": 3, "y": 4},
        {"x": 5, "y": 6},
        {"x": 7, "y": 8},
        {"x": 9, "y": 10},
    ]

    a_values = lambda a: (a["x"], a["y"])
    print(a_values(a[0]))

    # try simple one
    sum_lambda = lambda x, y: x + y
    print(sum_lambda(5, 6))

    # more simple one
    power_p = lambda q, p: pow(q, p)
    print(power_p(2, 4))

    num_list = [1, 4, 7]
    new_num_list = use_lambda_as_arg(num_list=num_list,
                                     func=lambda n: pow(n, 2))
    print(new_num_list)


def use_lambda_as_arg(num_list: List, func=None):
    return [func(num) for num in num_list]


if __name__ == "__main__":
    main()
