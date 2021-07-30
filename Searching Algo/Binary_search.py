def binary_search(arr, k):
    left=0
    right= len(arr)-1
    mid= len(arr)//2
    print(len(arr))
    while(left<=right):
        mid = (left + right) // 2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            left=mid+1
           # mid= (left+right)//2
        else:
            right=mid-1
          #  mid = (left + right)//2
    return -1

arr1=[3,4,2,9,19,22]
if __name__=='__main__':
   result=binary_search(arr1,22)
   if result != -1:
       print(f'The key was found in index {result}')
   elif result==-1:
       print("The key was not found in teh array")
