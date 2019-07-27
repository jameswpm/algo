#!/usr/bin/python3

def binary_search(list, item):
    low_index = 0
    high_index = len(list) - 1

    while low_index <= high_index:
        middle_index = (low_index + high_index) // 2
        guess = list[middle_index]
        if guess == item:
            return middle_index
        if guess > item:
            high_index = middle_index -1
        else:
            low_index = middle_index + 1
    return None