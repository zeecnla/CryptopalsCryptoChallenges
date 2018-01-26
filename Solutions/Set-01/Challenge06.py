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

def find_Key_Size(a):
    max_score = 0
    res = 0
    for key in range(2,41):
        first, second = a[key*5], a[key*10] 
        score = Hamming_Distance(first,second)/key
        if score > max_score:
            max_score = score
            res = key
    return res

def decodeBase64(t):
    return base64.b64decode(t)

  
def Break_Repeating_XOR():
    file_path = "H:\Projects\CryptopalsCryptoChallenges\Solutions\Set-01\\assets\\6.txt"    
    with open(file_path, "r") as f:
        lines = [line.strip('\n') for line in f]
        find_Key_Size(base64.b64decode(lines))

Break_Repeating_XOR()
