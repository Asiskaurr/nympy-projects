import sys
import numpy as np

myarr = np.array([[1,2,3],[4,5,6],[5,7,3]])       
print(myarr)              #to show the given array

print(myarr[1,2])         #to access any eliment of the array

print(myarr.shape)        #to know the shape of the given array

print(myarr.dtype)        #to know the datatype

print(myarr[1,2] == 6)    #to check the element

print(myarr.size)         #to know number of elements in the array

zeros = np.zeros((6,7))
print(zeros)              #to make an array of the given shape where every elemnt is 0

print(zeros.shape)

print(zeros.size)

print(zeros.dtype)
      
rng = np.arange(11)       #gives you an array from 0 to n-1
print(rng)                

lspace = np.linspace(2,9,17)      #gives you third digit's equally and linearly spaced elemnts between first two digit
print(lspace)

emp = np.empty((7,8))             #gives you an array of the given shape containing random elements which can be replaced with elements of your choice
print(emp)                        

emp_like = np.empty_like(myarr)   #gives an array of the same shape of the array mentioned containing random elements which can be replaced with elemnts of your choice 
print(emp_like)                  

ide = np.identity(56)             #gives an identity matrix of the given shape 
print(ide)

print(ide.shape)

print(ide.size)

print(ide.dtype)

arr = np.arange(72)
print(arr)

print(arr.reshape(12,6))         #will reshape the selected array into the given shape

print(arr.ravel())               #will reshape the selected array into a 1D array 

x = [[2,3,4],[5,7,8],[8,9,2]]    
ar = np.array(x)
print(ar)

sum = ar.sum(axis=0)             #will give sum along columns
print(sum)

sum2 = ar.sum(axis=1)            #will give sum along rows
print(sum2)

tp = ar.T                        #Will give transpose of the given matrix
print(tp) 

for item in ar.flat: print(item)             #will list all the elements 

nd = ar.ndim                                 #will tell the dimension of the given array
print(nd)

bt = ar.nbytes                               #tells you the total bytes consumed             
print(bt)

one = np.array([4, 95, 36, 19])

print(one.argmax())                          #tells the position at which the the greatest element is present 

print(one.argmin())                          #tells the position at which the the smallest element is present 

print(one.argsort())                         #gives an array of position of the elemnts in ascending order

print(ar.argmax())                           #gives the postion at which the largest element is present in the matrix 

print(ar.argmin())                           #gives the postion at which the smallest element is present in the matrix

print(ar.argmax(axis=0))                     #gives the position of the largest elements in the columns

print (ar.argmin(axis=0))                    #gives the position of the smallest elements in the columns

print(ar.argmax(axis=1))                     #gives the position of the largest elemts in the rows

print(ar.argmin(axis=1))                     #gives the position of the smallest elemts in the rows

print(ar.argsort())                          #gives an array of position of the elemnts in ascending order of the matrix

print (myarr + ar)                           #adds both the given matrixs

print(myarr * ar)                            #multiplies each element with one another

print(np.sqrt(ar))                           #gives an array of the square roots of each individual element

print(ar.sum())                              #gives sum of all the elements 

print(ar.max())                              #gives maximum no. of array

print(ar.min())                              #gives minimum no. of array

print(np.where(ar>7))                        #tells which element in the given matrix is greater than the given number

print(np.count_nonzero(ar))                  #counts the non zero elemnts in the given matrix

print(np.nonzero(ar))                        #tells you the position of all the non zero elements 

import sys

py_ar = [34,45,67,87]
np_ar = np.array(py_ar)
print(sys.getsizeof(1) * len(py_ar))        #tells the bytes consumed by python array

print(np_ar.itemsize * np_ar.size)          #tells the bytes consumed by numpy array