###

def cuddly_kittens(kittens, limit):
    n = len(kittens)
    max_len = 0
    
    for i in range(n):
        min_val = kittens[i]
        max_val = kittens[i]
        
        for j in range(i, n):
            min_val = min(min_val, kittens[j])
            max_val = max(max_val, kittens[j])
            
            if max_val - min_val <= limit:
                max_len = max(max_len, j - i + 1)
            else:
                break
    
    return max_len
