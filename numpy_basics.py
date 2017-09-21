import numpy as np

###############################################################################
### Lesson 1: Lists vs. Arrays -Difference b/w Numpy Array with Python List ###
###############################################################################
python_list = [1,2,3]
numpy_array = np.array([1,2,3])

#Appending
python_list.append(4) #result = [1,2,3,4]
python_list + [4] #result = [1,2,3,4] SAME

#Can't do appending with Arrays...so why use them? Ans. VECTORS


#1) The + operator does concatenation with lists, vector addition with Arrays

python_list2 = []
for e in python_list:
    python_list2.append(e + e) #result = [2,4,6,8]


numpy_array + numpy_array #result = [2,4,6,8]

2*numpy_array #result = [3,6,9,12]


#To represent a vector a numpy array is more intuitive than a python list
#List treated as array
#Array treated as VECTOR

###############################################################################
### Lesson 2: Dot Product -For Loop vs. Cos Function vs. Dot Function       ###
###############################################################################
a = np.array([1,2])
b = np.array([2,1])

#For loop Dot Product
dot = 0
for e,f in zip(a,b):
    dot += e*f #result = 4

#Vector Dot Product
(a*b).sum() #result = 4

#Numpy Dot Function
np.dot(a,b) #result = 4
a.dot(b)
b.dot(a) #all equal result

#Alternative Dot Product

###############################################################################
### Lesson 3: Vectors and Matrices                                          ###
###############################################################################
matrix = np.array([1,2], [3,4])
numpy_matrix = np.matrix([1,2], [3,4]) #not the same as array

#Note: Matrices NOT recommended as much as arrays -convert when you can:
np.array(numpy_matrix)


#Large array
np.random.random((10,10)) #arbitrary 10 X 10 array

#Gaussian Distribution
G = np.random.randn(10,10)

#Find the mean
G.mean()

#Find the variants
G.var()
