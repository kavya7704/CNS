#Reinforce Cipher
def Reinforce_Cipher(s):
    n = len(s)
    arr = [0] * len(s)
    j = 0
    for i in range(0,n-1,2):
        arr[j] = s[i]
        arr[n//2 + j] = s[i+1]
        j += 1
    
    if n % 2 != 0:
        arr.insert(j,s[-1])
        arr.pop()
        
    return arr
    
s = input()
print(Reinforce_Cipher(s))
