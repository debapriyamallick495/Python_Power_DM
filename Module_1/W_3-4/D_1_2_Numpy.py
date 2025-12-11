#creating a numpy array
import numpy as np
path = 'Module_1/W_3-4/assets/'
arr = np . array ([1,2,3,4,5])
print(arr)
print(type(arr))

#use a tuple to create a numpy array
arr1 = np . array ([1,2,3,4,5])
print(arr1)

#create nd array 
#0-D array
arr2 = np . array (1)
print ("0-D array:", arr2)

#1-D array
arr3 = np . array ([1,2,3])
print ("1-D array:", arr3)

#2-D array
arr4 = np . array ([[1,2,3,4,],[5,6,7,8]])
print ("2-D array:", arr4)

#3-D array
arr5 = np . array ([    [[1,2,3,4], [5,6,7,8]],
                    [[4,5,6,2],[7,8,9,10]]])
print ("3-D array:", arr5)

#save single array to .npy file
np.save (path +'data_a1.npy',arr3)
np.save (path +'data_a2.npy',arr4)
np.save (path +'data_a3.npy',arr5)
