"""
Find the ten most common words in Hamlet.txt

ref: https://docs.python.org/3/library/collections.html#collections.Counter
ref: https://developers.google.com/edu/python/regular-expressions#findall-with-files

"""

from collections import Counter
import re

# Find the ten most common words in Hamlet


def count_unique_words(filename):
    # your code here
    #words = re.findall(r'\w+', open(filename).read().lower())
    with open(filename, 'r') as f:
        content = f.read().lower()
    normalized = content.split(' ')
    list_of_ten = Counter(normalized).most_common(10)
    print(list_of_ten)
    # list_of_ten => [('the', 1136), ('and', 790), ('of', 738), ('to', 683), ('a', 541), ('in', 457), ('you', 453), ('my', 452), ('', 396), ('i', 360)]
    # hmm...'hamlet' ?  and '' = 396???  
    return list_of_ten


def print_list_of_ten(list_of_ten):
    for word in list_of_ten:
        print(f"{word[0]} {word[1]}")


if __name__ == '__main__':
    list_of_ten = count_unique_words('hamlet.txt')
    print_list_of_ten(list_of_ten)




"""
# Solution using the Regular Expression example in the Collections documentations

from collections import Counter
import re

def count_unique_words(filename):
    # your code here
    words = re.findall(r'\w+', open(filename).read().lower())
    list_of_ten = Counter(words).most_common(10)
    # list_of_ten => [('the', 1296), ('and', 1055), ('to', 828), ('of', 794), ('i', 635), ('you', 631), ('a', 624), ('in', 526), ('my', 516), ('hamlet', 476)]
    return list_of_ten

def print_list_of_ten(list_of_ten):
    for word in list_of_ten:
        print(f"{word[0]} {word[1]}")
        

if __name__ == '__main__':
    list_of_ten = count_unique_words('hamlet.txt')
    print_list_of_ten(list_of_ten)

"""
