# Created by Ishan Dindorkar on 12/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Use core Python regex to achieve text tokenization
"""
import re
from collections import namedtuple
from typing import Pattern


def main():
    pattern = create_master_pattern()

    text = "foo = 42"
    for token in generate_token(pattern, text):
        print(token)


def create_master_pattern():
    NAME = r"(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)"  # "?P<NAME>" is the syntax to assign name to a pattern
    NUM = r"(?P<NUM>\d+)"
    PLUS = r"(?P<PLUS>\+)"   # "+" is escaped here as it is a wildcard character in regex
    TIMES = r"(?P<TIMES>\*)"  # again "*" is escaped here as it is wildcard character in regex
    EQ = r"(?P<EQ>=)"
    WS = r"(?P<WS>\s+)"

    master_pattern = "|".join([NAME, NUM, PLUS, TIMES, EQ, WS])
    return re.compile(master_pattern)


def generate_token(pattern: Pattern, text):
    Token = namedtuple("Token", ["type", "value"])

    scanner = pattern.scanner(text)
    for match in iter(scanner.match, None):
        yield Token(match.lastgroup, match.group())


if __name__ == "__main__":
    main()

