def next_bigger(num):
    if int("".join(sorted(str(num), reverse=True))) == num:  
        return -1
    num_list= list(str(num)) 

    for i in range(len(num_list) -1, 0, -1):
        if num_list[i] > num_list[i-1]:     
            A=num_list[:i]
            B=num_list[i:]
            break                 

    B_list_for_min_num=sorted(list(B))   

    while B_list_for_min_num[0] <= A[-1]:    
        del B_list_for_min_num[0]  

    B[B.index(min(B_list_for_min_num))], A[-1] = A[-1], B[B.index(min(B_list_for_min_num))]
    B = sorted(B)

    finish = A + B
    result = int(''.join(map(str, finish)))
    
    return result 



print(next_bigger(2017))