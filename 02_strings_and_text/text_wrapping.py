# Created by Ishan Dindorkar on 12/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Text wrapping in Python to make long text read-friendly
"""
import textwrap


def main():
    long_text = """
    Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under.
    """
    print(textwrap.fill(long_text, 40))


if __name__ == "__main__":
    main()
