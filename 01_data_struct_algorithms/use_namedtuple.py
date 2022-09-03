# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Use of namedtuple
"""
from collections import namedtuple
from typing import List


def main():
    # 1. create list of stocks
    stock_list = create_stock_list()

    # 2. calculate portfolio worth
    total_value = calculate_portfolio_investment(stock_list)
    print(f"Total investment value: {total_value}")


def create_stock_list():
    apple_stock = ("APPL", 20, 612)
    ibm_stock = ("IBM", 10, 205)
    hp_stock = ("HP", 5, 37)

    return [apple_stock, ibm_stock, hp_stock]


def calculate_portfolio_investment(stock_list: List):
    total_value = 0
    Stock = namedtuple("Stock", ["name", "qty", "price"])  # defined namedtuple to represent a stock in portfolio

    for stock in stock_list:
        stock_inst = Stock(*stock)  # cast an ordinary tuple to an instance of namedtuple
        total_value += stock_inst.qty * stock_inst.price

    return total_value


if __name__ == "__main__":
    main()


"""
Discussion:
Use of nametuple instead of dictionary?
1. A namedtuple instance is immutable while that is not the case with dictionary
2. A namedtuple is efficient in terms of storage as compared to dictionary
3. A namedtuple can be altered using function "_replace()" but it will create a new instance of namedtuple
"""