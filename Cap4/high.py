#!/usr/bin/python3

'''
return highest value on a list (Ex. 4.3)
'''
def high(arr):
    if len(arr) == 1:
        return arr.pop(0)
    else:
        return max(arr.pop(0), high(arr))


'''
The book's answer for comparison
'''
def my_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = my_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print (high([222, 4, 6, 10, 20, 30]))
print (my_max([258, 259, 350, 1000, 2500, 259, 25]))