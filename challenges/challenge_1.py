#/usr/bin/python
# cryptopals crypto challenges
# Set 1: Basics
# - Challenge #1: Convert hex to base64
#   see https://cryptopals.com/sets/1/challenges/1

import base64

def main(hex_string: str) -> str:
    '''Converts hex encoded str -> bytes -> base64 encoded bytes -> str'''
    return base64.b64encode(bytes.fromhex(hex_string)).decode()
