#/usr/bin/python
# cryptopals crypto challenges
# Set 1: Basics
# - Challenge #2: Fixed XOR
#   see https://cryptopals.com/sets/1/challenges/2

def main(hex_string_a: str, hex_string_b: str) -> str:
    '''Converts two hex strings to bytes, XORs them and converts that back to
       hex'''
    bytes_a = bytes.fromhex(hex_string_a)
    bytes_b = bytes.fromhex(hex_string_b)

    # element-wise xor for the two byte arrays
    bytes_c = bytes(a ^ b for a, b in zip(bytes_a, bytes_b))
    return bytes_c.hex()
