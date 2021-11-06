def get_pairs_with_target_sum(arr, target):
    m = {}
    n = len(arr)
    count = 0

    for i in range(n):
        if target - arr[i] in m:
            count += m[target - arr[i]]
        
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
    
    return count