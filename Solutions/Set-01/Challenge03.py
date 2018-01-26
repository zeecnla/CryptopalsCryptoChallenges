# Set 1 Challenge 3
# Single-byte XOR cipher
import binascii
import base64




# http://www.stealthcopter.com/blog/2010/01/python-cryptography-decoding-a-caesar-shift-frequency-analysis/
freq = {"a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702,
        "f": 0.02228, "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153,
        "k": 0.00772, "l": 0.04025, "m": 0.02406, "n": 0.06749, "o": 0.07507,
        "p": 0.01929, "q": 0.00095, "r": 0.05987, "s": 0.06327, "t": 0.09056,
        "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150, "y": 0.01974,
        "z": 0.00074, " ": 0.19181}


def xorString(words, c):

    word = binascii.unhexlify(words)
    print(word)
    return ''.join(chr(num ^ c) for num in word)

def calculate_score(s):
    return sum([freq.get(c.lower(), 0) for c in s])


def xorCipher(encoded_string):
    decrypted=""
    max_score = 0
    char = 0

    for key in range(256):
        possible = xorString(encoded_string, key)
        score = calculate_score(possible)
        if score > max_score:
            decrypted, max_score, key = possible, score, key

    return decrypted


encoded_hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
result = xorCipher(encoded_hex_string)
answer = "Cooking MC's like a pound of bacon"
assert(result==answer), "Test 3, failed"


