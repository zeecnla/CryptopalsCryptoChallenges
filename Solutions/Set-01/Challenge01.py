# Set 1 Challenge 1
# Convert Hex to base64
import binascii
import base64

#operates in bytes
def HexToBase64(value):
    input_bytes = binascii.unhexlify(value) 
    output = base64.b64encode(input_bytes)
    return output
