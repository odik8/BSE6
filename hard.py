#!/usr/bin/env python3
# -*- coding utf-8 -*-

def common_letters():
    word1 = str(input("Введите слово: "))
    word2 = str(input("Введите второе слово: "))
    word3 = str(input("Введите третье слово: "))

    commons = []

    for i in word1:
        if i in word2 and i in word3 and i not in commons:
            commons.append(i)

    return commons


if __name__ == "__main__":
    print(f"Общие буквы: {common_letters()}")
