# Created by Ishan Dindorkar on 11/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Text formatting in Python
"""


def main():
    text = "Hello World"

    # 1. Shifting text left or right using "format"
    new_text = format(text, "^20")
    print(f"Original text: {text} | Formatted text: {new_text}")

    new_text = format(text, ">20")
    print(f"Original text: {text} | Formatted text: {new_text}")

    new_text = format(text, "<20")
    print(f"Original text: {text} | Formatted text: {new_text}")

    # 2. Use "format" to replace whitespace with character like *
    new_text = format(text, "*^20s")
    print(f"Original text: {text} | Formatted text: {new_text}")

    new_text = format(text, "=>20s")
    print(f"Original text: {text} | Formatted text: {new_text}")

    new_text = format(text, "=<20s")
    print(f"Original text: {text} | Formatted text: {new_text}")


if __name__ == "__main__":
    main()


"""
Discussion:
"format()" can work with any type of value - string or number.
Other options like str.rjust, str.ljust are not that much flexible.
"""