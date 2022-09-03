# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

from typing import List


def main():
    num_list = [1, 2, 3, 4, 5]
    print(f"List of numbers: {num_list}")

    head, *tail = num_list
    print(f"Head: {head}")
    print(f"Tail: {tail}")

    print(f"Sum of numbers: {add_tail_nums(head=head, tail=tail)}")


def add_tail_nums(head: int, tail: List):
    return head + sum(tail) if tail else head


if __name__ == "__main__":
    main()
