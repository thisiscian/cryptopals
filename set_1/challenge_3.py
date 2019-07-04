#!/usr/bin/python
# single-byte xor cipher
# https://cryptopals.com/sets/1/challenges/3

from string import ascii_letters, printable
from .generate_frequencies import score_string


def decode_single_xor(hex_string: str, alphabet: str = printable) -> str:
    best_score = None
    output = None
    str_bytes = bytes.fromhex(hex_string)
    for c in printable:
        h = ord(c)
        xor_bytes = bytes(b ^ h for b in str_bytes)
        try:
            xor_string = xor_bytes.decode('utf-8')
            score = score_string(xor_string)
            if score > 1:
                continue

            if best_score is None or best_score < score:
                best_score = score
                output = xor_string
        except UnicodeDecodeError:
            continue

    return output, best_score


def single_byte_xor_cipher(hex_string: str) -> str:
    output, best_score = decode_single_xor(hex_string)
    return output


def main():
    test_input = ('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783'
                  'a393b3736')
    test_output = "Cooking MC's like a pound of bacon"
    output = single_byte_xor_cipher(test_input)
    assert output == test_output


if __name__ == '__main__':
    main()
