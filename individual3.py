#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def paste_the_char():
    sentence = "Тестовое предложения для вставки вашей буквы"
    index_of_i = sentence.rfind('и')
    char = str(input("Введите символ: "))
    return sentence[:index_of_i] + char + sentence[index_of_i:]


if __name__ == "__main__":
    print(paste_the_char())
