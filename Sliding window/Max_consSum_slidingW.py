#finding the maximum sum of k consective elements in a given array
#solving this problem using sliding window

def max_sum(arr,k):
    n=len(arr)
    if n<k:
        print('Invalid operation')
        return  -1
    max_count=sum([arr[i] for i in range(0,k)])
    cur_count= max_count
    for j in range (0,n-k):
        cur_count= cur_count - arr[j] + arr[j+k]
        max_count= max(max_count,cur_count )
    return max_count

if __name__=='__main__':
    arr=[80,-50,100,90,200]
    print(max_sum(arr,2))