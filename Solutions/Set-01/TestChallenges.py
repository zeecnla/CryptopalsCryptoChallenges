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
    '''
    def test_challenge_3(self):
        encoded_hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        output = Challenge03.xorCipher(encoded_hex_string)
        answer = "Cooking MC's like a pound of bacon"
        self.assertEqual(output,answer)

    def test_challenge_4(self):
        
        file_path = "H:\Projects\CryptopalsCryptoChallenges\Solutions\Set-01\\assets\strings.txt"  
        output = Challenge04.detectSingleCharacterXOR(file_path)
        return 0 

    def test_challenge_5(self):
        self.assertEqual(1,1)

    def test_challenge_6(self):'''


if __name__ == '__main__':
    unittest.main()

