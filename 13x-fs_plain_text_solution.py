"""
# Find the ten most common words in Hamlet.txt

ref: https://docs.python.org/3/library/collections.html#collections.Counter
"""

from collections import Counter


def count_unique_words(filename='hamlet.txt'):
    words = Counter()
    # Extract the data into Python.
    with open(filename) as f:
        for line in f:
            words.update(line.split())
   

    # Calculate the ten most common words.
    for word, count in words.most_common(10):
        print(word, count)


if __name__ == '__main__':
    count_unique_words('hamlet.txt')
