def power_of(base,pwr):
    assert pwr >=0 and int(base)==base,'The power cant be negative and base should be integer'
    if pwr == 0:
        return 1
    elif pwr == 1:
        return base
    else:
        return base * power_of(base,pwr-1)
if __name__ == "__main__":
    print(power_of(-4,1))
