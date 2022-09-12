# Created by Ishan Dindorkar on 11/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Show efficient and inefficient ways of joining strings
"""


def main():
    str_parts = ["Is", "Chicago", "not", "Chicago?"]

    print(format("Efficient way of joining string parts", "*^20s"))
    combined_string = " ".join(str_parts)
    print(f"Combined string: {combined_string}")

    print(format("Inefficient way of joining string parts", "*^20s"))
    combined_string = ""
    for part in str_parts:
        combined_string += part + " "
    print(f"Combined string: {combined_string}")


if __name__ == "__main__":
    main()


"""
Discussion:
1. "+" operation on strings is bad as it creates new string objects and hence inefficient 
in terms of running time and space
2. join() operation is better than "+" 
"""