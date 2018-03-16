# Set 1 Challenge 5
# Implement Repeating-key XOR
import binascii
import base64

def RepeatingXOR(word, key):
    counter = 0
    encrypted_phrase= b''
    for letter in word:
        if(counter == len(key)):
            counter=0
        a = binascii.hexlify(letter.encode())
        b =binascii.hexlify(key[counter].encode())
        encrypted_phrase+=bytes([a^b])
        counter +=1





