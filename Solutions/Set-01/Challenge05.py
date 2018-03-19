# Set 1 Challenge 5
# Implement Repeating-key XOR
import binascii
import base64

def RepeatingXOR(word, key):
    counter = 0
    encrypted_phrase = ""
    for letter in word:
        if(counter == len(key)):
            counter=0
        a = ord(letter)
        b = ord(key[counter])
        encrypted_phrase+= (hex(a^b))
        counter +=1
    return encrypted_phrase

    





