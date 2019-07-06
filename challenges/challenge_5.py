#/usr/bin/python
# cryptopals crypto challenges
# Set 1: Basics
# - Challenge #5: Implement repeating-key XOR
#   see https://cryptopals.com/sets/1/challenges/5

def main(plain_string: str, key_string: str):
    '''encodes a given string with a given key, and returns a hex encoded
       string'''
    string_bytes = plain_string.encode()
    key_bytes = key_string.encode()
    l = len(key_bytes)

    xor_bytes = bytes(b ^ key_bytes[i % l] for i, b in enumerate(string_bytes))
    return xor_bytes.hex()
