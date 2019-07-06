#/usr/bin/python
# cryptopals crypto challenges
# Set 1: Basics
# - Challenge #4: Detect single-character XOR
#   see https://cryptopals.com/sets/1/challenges/4

from string import printable
from util import language_score

def main(hex_strings):
    '''Given newline separated hex_strings, detects the one that has been
       single-character XOR encoded'''

    best_score = 0
    best_xor = None
    for hex_string in hex_strings.splitlines():
        data = bytes.fromhex(hex_string)
        for char in printable:
            try:
                xor_string = bytes(a ^ ord(char) for a in data).decode()
            except UnicodeDecodeError:
                ### if we can't decode it, it definitely isn't human readable
                continue

            score = language_score(xor_string)

            if score > best_score:
                best_score = score
                best_xor = xor_string

    return best_xor
