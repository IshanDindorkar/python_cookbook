# Created by Ishan Dindorkar on 11/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Code to show text matching using regex
"""
import re
from calendar import month_abbr


def main():
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."
    print(f"Input text => {text}")

    # 1. Use regex to search for pattern in text string
    print(f"\n######## Simple text matching ########\n")
    date_pattern = re.compile(r"\d+/\d+/\d+")
    for match in re.finditer(date_pattern, text):
        print(match.group(0))

    # 2. Use regex pattern in the form of captured group to search for pattern in text string
    print(f"\n######## Captured group pattern matching ########\n")
    date_pattern_captured_group = r"(\d+)/(\d+)/(\d+)"
    for match in re.finditer(pattern=date_pattern_captured_group, string=text):
        for idx in range(4):
            print(f"{idx} => {match.group(idx)}")

    # 3. Use regex for substitution with the help of callback function
    print(f"\n######## Text substitution ########\n")
    compiled_pattern = re.compile(date_pattern_captured_group)
    new_text = compiled_pattern.sub(change_date, text)
    print(f"Substituted text: {new_text}")

    # 4. Explore greedy search behaviour of regex
    print(f"\n######## Greedy search using regex ########\n")
    text = """Computer says "no". Phone says "yes"."""
    print(greedy_search(text=text, allow_greedy_search=True))
    print(greedy_search(text=text, allow_greedy_search=False))

    # 5. Force "." to match newline character
    print(f"\n######## Use of re.DOTALL flag ########\n")
    text = """/* This is a
        multiline comment */"""
    print(dot_match_newline_char(text=text))


def change_date(match_obj: re.Match):
    """
    Helper function to change input date

    :param match_obj:
    :return:
    """
    mon_name = month_abbr[int(match_obj.group(1))]
    return f"{match_obj.group(2)} {mon_name} {match_obj.group(3)}"


def greedy_search(text: str, allow_greedy_search: bool):
    """
    Helper function to enable/disable greedy search behaviour of regex search

    :param text:
    :param allow_greedy_search:
    :return:
    """
    pattern = r"\"(.*)\""
    if not allow_greedy_search:
        pattern = r"\"(.*?)\""
    return re.findall(pattern=pattern, string=text)


def dot_match_newline_char(text: str):
    """
    Helper function to "force" .(period) regex wildcard character to recognize newline character

    :param text:
    :return:
    """
    pattern = r"/\*(.*?)\*/"  # to match all characters between /* .... */
    return re.findall(pattern=pattern, string=text, flags=re.DOTALL)


if __name__ == "__main__":
    main()


"""
Note: 
1. "." in regex can match any character but it do not match newline character i.e. "\n"
2. Flag re.DOTALL is useful to force "." to match newline character

"""