def pretty_birthday(s):
    l=s.upper().split(';')

    temp = []
    for i in l:
        i_temp='(%s, %s)'%(i.split(':')[1], i.split(':')[0])
        temp.append(i_temp)
    
    temp.sort()
    s_res = ''.join(temp)

    return s_ress