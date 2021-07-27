def my_fact(n):
    assert n>=0 and int(n)== n, 'The number is less than zero'
    if n in [0,1]:
        return 1
    else:
        return n * my_fact(n-1)

if __name__ == '__main__':
    g= int(input('Enter the number for factorial:'))
    fact= my_fact(g)
    print(fact)