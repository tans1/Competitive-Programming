t = int(input())
for _ in range(t):
    x = int(input())
    
    bn = list(bin(x).lstrip('0b'))
    bn.reverse()
    j = 1
    
    i = 0
    while i < len(bn) and bn[i] == '0':
        j = j<<1
        i += 1
    
        
    if (j^x) > 0 :
        print(j)
    else:
        k = 1
        i = 0
        while i < len(bn) and bn[i] == '1':
            k = k<<1
            i += 1
        
        print(k|j)
