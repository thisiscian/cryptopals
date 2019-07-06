#!/usr/bin/python
# fixed xor
# https://cryptopals.com/sets/1/challenges/2

from ..util import XOR, BytesConverter

def main():
    test_inputs = [
        '1c0111001f010100061a024b53535009181c',
        '686974207468652062756c6c277320657965'
    ]
    test_output = '746865206b696420646f6e277420706c6179'
    output_bytes = XOR.auto(*test_inputs)
    output = BytesConverter.toHexString(output_bytes)
    
    assert output == test_output


if __name__ == '__main__':
    main()
