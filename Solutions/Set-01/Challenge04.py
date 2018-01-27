#Set 1 Challenge 4
#Detect single-character XOR
import Challenge03


def detectSingleCharacterXOR():
    decrypted=""
    max_score = 0
    char = 0
    file_path = "H:\Projects\CryptopalsCryptoChallenges\Solutions\Set-01\\assets\strings.txt"    
    with open(file_path, "r") as f:
        
        lines = [line.strip('\n') for line in f]
        for line in lines:
            possible = Challenge03.xorCipher(line)
            score = Challenge03.calculate_score(possible)
            if score > max_score:
                decrypted, max_score = possible, score

    return decrypted