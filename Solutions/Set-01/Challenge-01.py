# Set 1 Challenge 1
# Convert Hex to base64
import binascii
print("Set 1 - Challenge 1: ")

answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bytes_string = binascii.unhexlify(hex_string)
message = binascii.b2a_base64(bytes_string)

print(message.decode("utf-8"));
assert(message == answer)
