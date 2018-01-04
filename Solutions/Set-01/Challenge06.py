#Break repeating key XOR
import base64
import binascii


def Hamming_Distance(a,b):
    assert len(a)==len(b)
    a = ''.join([bin(ord(x))[2:].zfill(8) for x in a])
    b = ''.join([bin(ord(x))[2:].zfill(8) for x in b])
    i = 0
    counter = 0
    while i != len(a):
        if(a[i] != b[i]):
            counter = counter + 1
        i = i+1
    return counter
  
def Break_Repeating_XOR():
    
    #Length of the key
    keysize = (list(bytes(range(2,41))))
    print(keysize)
    file_path = "H:\Projects\CryptopalsCryptoChallenges\Solutions\Set-01\\assets\\6.txt"    
    #with open(file_path, "r") as f:
     
Break_Repeating_XOR()
