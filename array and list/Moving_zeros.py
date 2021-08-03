#program to move zeros to the end
def mov_zeros(arr):
    i=0
    for num in arr:
        if num!=0:
            arr[i]=num
            i+=1
    for i in range(i,len(arr)):
        arr[i]=0
    return arr

if __name__=='__main__':
    print(mov_zeros([1,2,0,0,4,0,6]))
