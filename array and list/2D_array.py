import numpy as np

arr1 = np.array([[4,5,6,7,1],[2,9,0,1,3],[6,3,0,3,4]])
print(arr1)
#time complexity is O(1)
#space complexity is O(mn)

#to add a new row or column in the begining
new_arr= np.insert(arr1,0,[[1,2,3,4,5]],axis=0)
#print(new_arr)

#to add new row or coulmn at the end

new_arr1= np.append(arr1,[[5,6,7,8,9]],axis=0)
#print(new_arr1)
 #for deleting 1st row or column

new_arr2= np.delete(arr1,0,axis=1)
print(new_arr2)