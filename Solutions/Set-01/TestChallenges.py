
#File used to test that the challenges work
import Challenge01
import Challenge02
import Challenge03
import Challenge05
import binascii
import base64

def Challenge_1_Test():
    answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    input_ = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    output = Challenge01.HexToBase64(input_)
    assert answer == output, "Test 1, failed"


def Challenge_2_Test():
    firstString = "1c0111001f010100061a024b53535009181c"
    secondString = "686974207468652062756c6c277320657965"
    answer = "746865206b696420646f6e277420706c6179"
    output = Challenge02.XOROperation(firstString, secondString)
    assert(answer==output), "Test 2, failed"

def Challenge_3_Test():
    encoded_hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    result = Challenge03.xorCipher(encoded_hex_string)
    answer = "Cooking MC's like a pound of bacon"
    assert(result==answer), "Test 3, failed"

def Challenge_5_Test():
    phrase = Challenge05.RepeatingXOR(b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal''',b'ICE') 
    result = binascii.hexlify(phrase).decode('ascii')
    answer = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    assert(result==answer), "Test 5 failed"


Challenge_1_Test()
Challenge_2_Test()
Challenge_3_Test()
Challenge_5_Test()

