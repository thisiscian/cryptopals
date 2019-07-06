#!/usr/bin/python
# convert hex to base64
# https://cryptopals.com/sets/1/challenges/1

from base64 import b64encode
from ..util import HexStringConverter


def main():
    test_input = ('49276d206b696c6c696e6720796f757220627261696e206c696b6520612'
                  '0706f69736f6e6f7573206d757368726f6f6d')
    test_output = ('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2'
                   'hyb29t')
    output = HexStringConverter.toBase64(test_input)
    assert test_output == output


if __name__ == '__main__':
    main()
