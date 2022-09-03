# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Dictionary operations like finding minimum, maximum value or sorting based on value
"""
from typing import Dict
from loguru import logger


def main():
    # 1. create dictionary
    prices = create_dictionary()
    logger.info(f"Inversion of dictionary: {zip(prices.values(), prices.keys())}")

    # 2. sort dictionary
    sorted_prices = sort_dictionary(prices=prices)
    logger.info(f"Prices in sorted order: {sorted_prices}")

    # 3. find minimum value from dictionary
    min_val = find_min_value(prices=prices)
    logger.info(f"Minimum share value: {min_val}")

    # 4. find maximum value from dictionary
    max_val = find_max_value(prices=prices)
    logger.info(f"Maximum share value: {max_val}")


def create_dictionary():
    prices = {
        "ACME": 45,
        "AAPL": 612,
        "IBM": 206,
        "HPQ": 37,
        "FB": 11,
    }

    return prices


def sort_dictionary(prices: Dict):
    return sorted(zip(prices.values(), prices.keys()))


def find_min_value(prices: Dict):
    return min(zip(prices.values(), prices.keys()))


def find_max_value(prices: Dict):
    return max(zip(prices.values(), prices.keys()))


if __name__ == "__main__":
    main()
