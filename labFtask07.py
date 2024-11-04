import numpy as np
numbers = np.array ([2, 3, 5, 7, 11])
print(numbers)

import numpy as np
num = np.array([10,20,30])
print(num)
print(type(num))

array_1D = np.array([2,4,5,6])
print(array_1D)

array_2D = np.array([[2,4,5,6],[2,4,5,6],[2,4,5,6]])
print(array_2D)

array_3D = np.array([[[2,4,5,6],[2,4,5,6],[2,4,5,6]]])
print(array_3D)

output = np.array([[x for x in range(2,21,2)],[x for x in range(1,21,2)]])
print(output)

ary = np.array([[1,2,3], [4,5,6]])
print(ary)
print(ary.dtype)
print(ary.ndim)
print (ary.shape)
print(ary.size)
print(ary.itemsize)

ary = np.array([[1,2,3],[4,5,6]])
print(ary)
print(ary>5)
print(ary<5)
print(ary==5)

grades = np.array([[87,96,70], [100,67,90],
                    [94,77,90],[100,81,82]])
print(grades)
print(grades.max())
print(grades.sum())
print(grades.std())
print(grades.mean())
print(grades.var())
print(grades.mean(axis=0))
print(grades.mean(axis=1))

num1= np.arange(1,6)
print(num1)
num2= num1.view()
print(num2)
print(id(num1))
print(id(num2))
num2[1]*=5
print(num1)
print(num2)

num1= np.arange(1,6)
print(num1)
num2= num1.copy()
print(num2)
print(id(num1))
print(id(num2))
num2[1]*=5
print(num1)
print(num2)

#1
score = np.array([85,90,78,92,88])
score1 = score.astype('f')
print(score)
print(score1)

#2
a_score = score.copy()
print(a_score + 5)

#3
print(score.shape)
print(score.ndim)
print(score.size)
print(score.itemsize)
print(score.dtype)
score.sort()
print(score)

#4
x = np.where(score>80)
print(x)

#5
print(score.max())
print(score.min())
print(score.std())
print(score.var())
print(score.sum())
print(score.mean())
print(score.mean(axis=0))

#6
print(score[::2])
print(score[-3:-1])
print(score[1:4])


