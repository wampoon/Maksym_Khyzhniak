def digital_root(num):
    while num >= 10:
        num = sum(int(i) for i in str(num))
    return num