# Set 1 Challenge 1
# Convert Hex to base64
import binascii, base64
print("Set 1 - Challenge 1: ")

answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
input_ = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

encoded_string = str.encode(input_);
input_bytes = binascii.unhexlify(encoded_string)
output = base64.b64encode(input_bytes)

print("Input: \n"+input_)
print("Output: \n"+output)
assert(output == answer)
