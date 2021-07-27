def my_fib(n):
    assert n>=0 and int(n)==n, 'fibonacci number cannot be less than 0 or non integer'
    if n in [0,1]:
        return n
    else:
        return my_fib(n-1)+ my_fib(n-2)

if __name__ =='__main__':
    print(my_fib(6))
    print('I am thinking of you too baby')
    #New comment
