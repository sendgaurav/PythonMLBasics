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
