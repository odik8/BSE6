#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
    sentence = str(input("Enter the sentence: "))
    symbol1 = str(input("Enter first symbol to find: "))
    symbol2 = str(input("Enter second symbol to find: "))

    return f"Count of '{symbol1}' symbol and '{symbol2}' symbol is {sentence.count(symbol1) + sentence.count(symbol2)}"

if __name__ == "__main__":
    print(main())
