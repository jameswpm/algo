#!/usr/bin/python3

'''
Recursive function to count the number of elements in a list (Ex. 4.2)
'''
def my_count(arr):
    if len(arr) == 1:
        return 1
    else:
        arr.pop()
        return 1 + my_count(arr)

print (my_count([2, 4, 6, 10, 20, 30]))