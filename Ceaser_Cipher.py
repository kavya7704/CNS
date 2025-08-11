#Encoding
def Ceaser_Cipher(s,k):
    
    new = ''
    for i in s:
        temp = chr((ord(i) + k))
        new += temp
        
    return new
    
s = input()
k = int(input())
print(Ceaser_Cipher(s,k))

#Decoding
def Ceaser_Cipher(s,k):
    
    new = ''
    for i in s:
        temp = chr((ord(i) - k))
        new += temp
        
    return new
    
s = input()
k = int(input())
print(Ceaser_Cipher(s,k))
