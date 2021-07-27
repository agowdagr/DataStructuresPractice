def sumofdigits(n):
    assert n>=0 and int(n)== n ,'n is not a positive or integer'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofdigits(int(n/10))
if __name__ == '__main__':
    print(sumofdigits(22))