#/usr/bin/python
# cryptopals crypto challenges
# Set 1: Basics
# - Challenge #3: Single-byte XOR cipher
#   see https://cryptopals.com/sets/1/challenges/3

from string import printable
from util import language_score

def main(hex_string):
    '''Guesses the correct single char encryption for a given hex string'''

    best_score = 0
    best_xor = None
    data = bytes.fromhex(hex_string)
    for char in printable:
        # ord(x) gets the integer value of a character, equivalent to a single
        # byte
        xor_string = bytes(a ^ ord(char) for a in data).decode()

        score = language_score(xor_string)

        if score > best_score:
            best_score = score
            best_xor = xor_string

    return best_xor

if __name__ == "__main__":
    main()
