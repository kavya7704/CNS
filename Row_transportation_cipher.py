def Row_transportation_cipher(s,key):
    n = len(key)
    arr = [[0 for i in range(n)]for j in range(n+1)]
    
    d = {}
    print(s)
    for i in range(n):
        if key[i] not in d:
            d[key[i]] = i
            
    arr[0] = key
    k = 0
    for i in range(1,n):
        for j in range(0,n):
            if k < len(s):
                arr[i][j] = s[k]
                k += 1
            else:
                break
            
    key.sort()
    cipher = '' 
    for val in key:
        k = d[val]
        for j in range(1,n):
            if arr[j][k] != 0:
                cipher += arr[j][k]
            else:
                break

    return cipher
    
s = input()
key = list(map(int,input().split()))
print(Row_transportation_cipher(s,key))
