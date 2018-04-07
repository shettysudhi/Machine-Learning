import numpy as np

my_list = [1,2,3,4,5] #python list
arr = np.array(my_list) #one dimension array
print(my_list)
print(arr)


my_list = [[1,2,3], [4,5,6], [7,8,9]] #list of list
arr = np.array(my_list)
print(my_list)
print(arr)

'''
output
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

print(np.arange(0, 10))
print(np.arange(0, 10, 2)) #step size 2
print(np.zeros(3)) #vector with one row, 3 column
print(np.zeros((2,3))) # tuple (2,3) says 2 row and 3 colum

'''
output
[ 0.  0.  0.]
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
'''

print(np.ones((2,3)))


print(np.linspace(0,6,10)) #one dim array with 10 element, evenly spaced point distributed b/n 0 to 6

print(np.eye(3))#Identity matrix -> num of row same as column
'''
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
'''


print(np.random.rand(3)) #Random number, uniformly distributed 0 to 1
print(np.random.rand(3,3)) #Two dim array with Random number, uniformly distributed 0 to 1

print(np.random.randn(100)) #One dim array, random points distributed around 0.
print(np.random.randn(10,10)) #Two dim array, random points distributed around 0.

print(np.random.randint(0, 10)) #One random num b/n 0 to 9
print(np.random.randint(0, 10, 3)) #Three random num b/n 0 to 9

arr = np.arange(25);
print(arr)
print(arr.reshape(5,5))   # 5 * 5 = 25

arr = np.random.randint(0, 10, 15);
print(arr.max())
print(arr.min())

print(arr.argmax()) # index of max element
print(arr.argmin()) # index of min element
print(arr)

arr = np.random.randint(0, 99, 10)
print(arr.shape)
arr = arr.reshape(2,5)
print(arr.shape)

'''
output
(10,)  # vector
(2, 5) # 2 dim array
'''

print(arr.dtype)
'''
int32  # 32 bit int
'''

from numpy.random import randint # instead of random.randint
randint(2, 7)






