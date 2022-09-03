# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

from operator import itemgetter


def main():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]

    sorted_rows = sorted(rows, key=itemgetter("uid"))
    print(f"Rows sorted: {sorted_rows}")


if __name__ == "__main__":
    main()
