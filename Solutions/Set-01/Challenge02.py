# Set 1 Challenge 2
# Fixed XOR
import binascii
import base64

def XOROperation(a, b):
    if(len(a) == len(b)):
        output = int(a,16) ^ int(b,16)
        return format(output, 'x')
    else:
        return False
