def my_gcp(a,b):
    assert int(a)==a and int(b)==b,'The nubers a , b must be integers'
    if a<0:
        a= -1*a
    if b<0:
        b=-1*b
    if b==0:
        return a
    else:
        return my_gcp(b,a % b)
print(my_gcp(48,-18))