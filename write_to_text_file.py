#!/usr/bin/env python
"""
Example file.
"""

FRUITS = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]

def main():
    """
    Program entry point

    :return:
    """
    with open('fruitdata.txt', 'w') as fruitdata_out:
        for fruit in FRUITS:
            fruitdata_out.write(fruit + '\n')

if __name__ == '__main__':
    main()
