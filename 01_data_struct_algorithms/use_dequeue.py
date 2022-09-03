# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Code showing use of deque
"""
from collections import deque
from typing.io import TextIO


def main():
    with open("dequeue_demo.txt") as file:
        for line, prev_lines in search_pattern(file, "python", 2):
            for pline in prev_lines:
                print(pline)
            print(line)
            print("================================")


def search_pattern(lines: TextIO, pattern: str, history: int):
    prev_lines = deque(maxlen=history)  # to hold history of lines scanned
    for line in lines:
        if pattern in str(line).lower():
            yield line, prev_lines
        prev_lines.append(line)


if __name__ == "__main__":
    main()

"""
Discussion: Deque
q = deque(maxlen=3)
q.append(1)
q.append(2)

Unbounded deque =>
q = deque()
q.append(1)
q.appendleft(2) => append elements from left
q.pop() => remove element from right by default
q.popleft() => remove element from left
 
"""