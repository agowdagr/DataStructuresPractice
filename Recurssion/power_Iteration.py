def pow_iter(base,pwr):
    assert pwr>=0 and int(base)==base,'pwr needs to be postive and base needs to be integer'
    i=0
    result= 1
    while i<pwr:
        result= result*base
        i+=1
    return result
if __name__=='__main__':
    print(pow_iter(-4,1))
