import Challenge01
import Challenge02
import Challenge03
import Challenge04
import Challenge05
import unittest


# Will begin to review the challenges to finally complete them 
class TestChallengesSet1(unittest.TestCase):
    def test_challenge_1(self):
        answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        input_ = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        output = Challenge01.HexToBase64(input_)
        solution = output.decode("utf-8")
        self.assertEqual(solution,answer)
    

    def test_challenge_2(self):
        firstString = "1c0111001f010100061a024b53535009181c"
        secondString = "686974207468652062756c6c277320657965"
        answer = "746865206b696420646f6e277420706c6179"
        output = Challenge02.XOROperation(firstString, secondString)
        self.assertEqual(output,answer)
    
    def test_challenge_3(self):
        encoded_hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        output = Challenge03.xorCipher(encoded_hex_string)
        answer = "Cooking MC's like a pound of bacon"
        self.assertEqual(output,answer)
    
    def test_challenge_4(self):
        file_path = "C:\\Users\\Admin\Documents\\GitHub\\CryptopalsCryptoChallenges\\Solutions\\Set-01\\assets\\strings.txt"  
        output = Challenge04.detectSingleCharacterXOR(file_path)
        answer = "Now that the party is jumping\n"
        self.assertEqual(output,answer)

    def test_challenge_5(self):
        key = 'ICE'
        phrase = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
        answer = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''
        output = Challenge05.RepeatingXOR(phrase,key)
        self.assertEqual(output,answer)
    '''
    def test_challenge_6(self):'''


if __name__ == '__main__':
    unittest.main()

