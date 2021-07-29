def findmax_recursive(samplearray, n):
    if n==1:
        return samplearray[0]
    else:
        return max(samplearray(n-1), findmax_recursive(samplearray,n-1))