import numpy as np

#Indexing
arr = np.arange(1, 11)
'''
[ 1  2  3  4  5  6  7  8  9 10]
'''
print(arr[8]) # element at index 8
'''
9
'''
print(arr[1:5]) #return elements from index 1 to 4
'''
[2 3 4 5]
'''
print(arr[:3]) #everything up to 3, same as arr[0,3]
'''
[1 2 3]
'''
print(arr[5:]) #beyond 5, inclusive 5
'''
[ 6  7  8  9 10]
'''
arr[0:5] = 99 # broadcast 1 to 5 with 100
print(arr)
'''
[99 99 99 99 99  6  7  8  9 10]
'''

#How slicing works
arr = np.arange(1,11)
'''
[ 1  2  3  4  5  6  7  8  9 10]
'''
slice_0_to_5 = arr[0:5] # data is not copied, its just view
'''
[1 2 3 4 5]
'''
slice_0_to_5[:] = 25 # broadcast 25
print(arr)
'''
[25 25 25 25 25  6  7  8  9 10]
'''

arr_copy = arr.copy()
arr_copy[:] = 0 # this un-effect original array

# Continue......
