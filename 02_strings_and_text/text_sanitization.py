# Created by Ishan Dindorkar on 06/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Show examples of text sanitization with Unicode characters
"""
import sys
import unicodedata


def main():
    text = "pýtĥöñ\fis\tawesome\r\n"
    print(f"Input text: {text}")

    # 1. Remove/replace sequence of characters from input text
    remap = {
       ord("\t"): " ",
       ord("\f"): " ",
       ord("\r"): None
    }
    new_text = text.translate(remap)
    print(f"Modified text with chunks(like carriage return etc.) replaced: {new_text}")

    # 2. Handle unicode characters
    new_text = unicodedata.normalize("NFD", new_text)

    cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode)
                              if unicodedata.combining(chr(c)))  # combining characters
    updated_text = new_text.translate(cmb_chars)
    print(f"After handling unicode characters: {updated_text}")


if __name__ == "__main__":
    main()
