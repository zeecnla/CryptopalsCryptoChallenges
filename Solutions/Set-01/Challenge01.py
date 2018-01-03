# Set 1 Challenge 1
# Convert Hex to base64
import binascii
import base64

def HexToBase64(input_):
    encoded_string = str.encode(input_)
    input_bytes = binascii.unhexlify(encoded_string)
    output = base64.b64encode(input_bytes)
    return output.decode()
