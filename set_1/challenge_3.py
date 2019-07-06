#!/usr/bin/python
# single-byte xor cipher
# https://cryptopals.com/sets/1/challenges/3

from .. import util
from string import ascii_letters, printable


def decode_single_xor(hex_string: str) -> str:
    best_score = None
    output = None
    for c in printable:
        try:
            xor_string = util.XOR.toString(hex_string, c)
            score = util.score_string(xor_string)

            if best_score is None or best_score < score:
                print(score, output)
                best_score = score
                output = xor_string
        except UnicodeDecodeError:
            continue

    return output, c, best_score


def single_byte_xor_cipher(hex_string: str) -> str:
    score, char, output = util.guess_decode_single_character_xor(hex_string)
    return output


def main():
    test_input = ('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783'
                  'a393b3736')
    test_output = "Cooking MC's like a pound of bacon"
    output = single_byte_xor_cipher(test_input)
    assert output == test_output


if __name__ == '__main__':
    main()
