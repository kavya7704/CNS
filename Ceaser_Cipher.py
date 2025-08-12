#Encoding
def Ceaser_Cipher(s,k):
    
    new = ''
    for i in s:
        temp = chr((((ord(i) - 65 + k)) % 26)+65)
        new += temp
        
    return new
    
s = "HELLO"
k = 88
print(Ceaser_Cipher(s,k))

#Decoding
def Ceaser_Cipher(s,k):
    
    new = ''
    for i in s:
        temp = chr((((ord(i) - 65 - k)) % 26)+65)
        new += temp
        
    return new
    
s = input()
k = int(input())
print(Ceaser_Cipher(s,k))
