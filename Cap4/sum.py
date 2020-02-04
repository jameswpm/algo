#!/usr/bin/python3

'''
Recursive function to sum the values of an array (Ex. 4.1)
'''
def sum(arr):
    if len(arr) == 1:
        return arr.pop(0)
    else:
        return arr.pop(0) + sum(arr)

print (sum([2, 4, 6, 10, 20, 30]))