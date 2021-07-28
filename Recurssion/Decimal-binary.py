def decimal_binary(n):
    assert int(n)==n,'The number should be integer'
    if n==0:
        return 0
    else:
        return n % 2+ 10* decimal_binary(int(n/2))
print (decimal_binary(5))