# Set 1 Challenge 1
# Convert Hex to base64
import binascii
import base64
import codecs

def HexToBase64(value):

    encoded_string = str.encode(value)
    input_bytes = binascii.unhexlify(encoded_string) 
    output = base64.b64encode(input_bytes)
    return output
