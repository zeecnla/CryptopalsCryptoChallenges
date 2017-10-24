
# Set 1 Challenge 2
# Fixed XOR
import binascii, base64
print("Set 1 - Challenge 2: ")


def XOROperation(a, b):
    output = int(a,16) ^ int(b,16)
    return format(output, 'x')

s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"
answer = "746865206b696420646f6e277420706c6179"
if len(s1) == len(s2):
    output = XOROperation(s1, s2)
    assert(answer==output)
