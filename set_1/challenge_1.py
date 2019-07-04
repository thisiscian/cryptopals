#!/usr/bin/python
# convert hex to base64
# https://cryptopals.com/sets/1/challenges/1

from base64 import b64encode


def hex_string_to_base64(hex_string: str) -> str:
    hex_bytes = bytes.fromhex(hex_string)
    b64_bytes = b64encode(hex_bytes)
    return b64_bytes.decode('utf-8')


def main():
    test_input = ('49276d206b696c6c696e6720796f757220627261696e206c696b6520612'
                  '0706f69736f6e6f7573206d757368726f6f6d')
    test_output = ('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2'
                   'hyb29t')
    output = hex_string_to_base64(test_input)
    assert test_output == output


if __name__ == '__main__':
    main()
