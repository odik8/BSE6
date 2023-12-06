#!/usr/bin/env python3

def common_letters(word1, word2, word3):
    set1 = set(word1)
    set2 = set(word2)
    set3 = set(word3)

    common_letters_set = set1.intersection(set2, set3)

    print("Общие буквы:", ", ".join(common_letters_set))


if __name__ == "__main__":
    common_letters("1Kawazaki", "1iCago", "1Kricko")
