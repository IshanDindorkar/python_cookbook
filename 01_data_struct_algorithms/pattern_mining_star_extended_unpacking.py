"""
Unpack iterable based on pattern matching
"""
from typing import List


def main():
    records = [
        ("foo", 1, 2),
        ("bar", "Hello"),
        ("foo", 3, 4)
    ]

    for tag, *payload in records:
        if tag == "foo":
            do_foo(payload)
        elif tag == "bar":
            do_bar(payload)
        else:
            pass


def do_foo(seq: List):
    print(f"foo | {seq}")


def do_bar(seq: List):
    print(f"bar | {seq}")


if __name__ == "__main__":
    main()
