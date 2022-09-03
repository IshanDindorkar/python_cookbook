# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Use collections.Counter data structure to get counts of different elements in a sequence
"""
from collections import Counter


def main():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
        ]

    word_counter = Counter(words)
    print(f"Top 3 words: {word_counter.most_common(3)}")


if __name__ == "__main__":
    main()
