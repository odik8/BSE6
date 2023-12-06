#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_words(sequence):
    correct_words = []
    incorrect_words = []
    corrected_words = []

    for word in sequence:
        if "чя" in word or "щя" in word:
            incorrect_words.append(word)
        else:
            correct_words.append(word)

    for word in incorrect_words:
        if "чя" in word and "щя" in word:
            corrected_words.append(word.replace("чя", "ча").replace("щя", "ща"))
        if "чя" in word and "щя" not in word:
            corrected_words.append(word.replace("чя", "ча"))
        if "чя" not in word and "щя" in word:
            corrected_words.append(word.replace("щя", "ща"))

    print("\nСлова с ошибкой в записи буквосочетания \"ча\" или \"ща\":")
    for word in incorrect_words:
        print(f'  "{word}"')

    print("\nИсправленные слова:")
    for word in corrected_words:
        print(f'  "{word}"')




if __name__ == "__main__":
    word_sequence = [
        "чяй", "чайник", "чашка", "чящя", "роща", "щявель",
        "выручай", "гущя", "часто", "час", "чясы", "часовой",
        "чайка", "тучя", "чюгун", "хочу", "часть", "чуб",
        "чудо", "учу", "щука", "щуплый"
    ]

    check_words(word_sequence)
