import numpy as np
import random 
#Zeros array
n1 = np.zeros((1,2))
print(n1)

#two dimensional aaray
n2 = np.array([[1,2,3,4],[4,3,2,1]])
print(n2)

#One dimensional array
n3 = np.array([1,2,3,4,5,6])

#Random Numbers
n4 = np.random.randint(1,100,5)
print(n4)

#Arange Method
n5 = np.arange(10,20)
print(n5)

#Shape of array
n6 = n2.shape
print(n6)

# vstack method and hstack method
n7 = np.array([1,2,3,4])
n8 = np.array([5,6,7,8])
print("Vertical Stacking of arrays:")
n9 = np.vstack((n7,n8))
print(n9)

print("Horizontal Stacking of arrays:")

n10 = np.hstack((n7,n8))
print(n10)

#Sum of arrays 
n11 = np.sum([n7,n8],)
print(n11)

#Basic Operations 
n12 = n7 + 2
print(n12)
n13 = n7 *2
print(n13)