#!/usr/bin/python3

'''
Get an array and return the index of smaller value, compared with all other ones
'''
def searchLess(arr):
    less = arr[0]
    less_index = 0
    for i in range(1, len(arr)):
        if arr[i] < less:
            less = arr[i]
            less_index = i
    return less_index

'''
The selection sort algorithm.
'''
def selectionSort(arr):
    new = []
    for i in range(len(arr)):
        less = searchLess(arr)
        new.append(arr.pop(less))
    return new

print (selectionSort([5, 3, 6, 2, 10]))

