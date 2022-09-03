# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Code to show use of heapq
"""
import heapq


def main():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nsmallest(3, nums))
    print(heapq.nlargest(3, nums))

    cheap, expensive = find_cheap_expensive_stocks()
    print(f"Cheap stocks: {cheap}")
    print(f"Expensive stocks: {expensive}")


def find_cheap_expensive_stocks():
    portfolio = [
        {"name": "IBM", "shares": 100, "price": 91.1},
        {"name": "AAPL", "shares": 50, "price": 543.22},
        {"name": "FB", "shares": 200, "price": 21.09},
        {"name": "HPQ", "shares": 35, "price": 31.75},
        {"name": "YHOO", "shares": 45, "price": 16.35},
        {"name": "ACME", "shares": 75, "price": 115.65},
    ]

    cheap = heapq.nsmallest(1, portfolio, key=lambda s: s["price"])
    expensive = heapq.nlargest(1, portfolio, key=lambda s: s["price"])

    return cheap, expensive


if __name__ == "__main__":
    main()


"""
Discussion: heapq
Data structure useful to find N smallest or largest elements from a collection when 
N is small as compared to the size of collection itself
"""