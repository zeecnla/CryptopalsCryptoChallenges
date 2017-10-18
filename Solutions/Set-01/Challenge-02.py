# Set 1 Challenge 2
# Fixed XOR
print("Set 1 - Challenge 2: ")
def XOROperation(a, b):
    result = hex(int(a,16)^ int(b, 16))
    return result

the_string =    "1c0111001f010100061a024b53535009181c"
second_string = "686974207468652062756c6c277320657965"
print(XOROperation(the_string, second_string))
