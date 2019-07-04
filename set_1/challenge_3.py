#!/usr/bin/python
# single-byte xor cipher
# https://cryptopals.com/sets/1/challenges/3

from string import printable
from .generate_frequencies import main as get_frequency

printable_frequency = get_frequency()

def get_frequency(string: str) -> list:
    output = [0] * len(printable_frequency)
    for l in string:
        if not l in printable_frequency:
            continue

        index = printable_frequency.index(l)
        output[index] += 1
    return output

def score_frequency(frequency: list) -> float:
    output = 0
    resorted = sorted(enumerate(frequency), key=lambda v: v[1], reverse=True)
    for i, I in enumerate(resorted):
        j, v = I
        output += abs(i - j)

    return output

def single_byte_xor_cipher(hex_string: str) -> str:
    best = None
    output = None
    str_bytes = bytes.fromhex(hex_string)
    for c in printable:
        h = ord(c)
        xor_bytes = bytes(b ^ h for b in str_bytes)
        xor_string = xor_bytes.decode()
        freq = get_frequency(xor_string)
        score = score_frequency(freq)
        if best is None or best > score:
            best = score
            output = xor_string

    return output

def main():
    test_input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    test_output = "Cooking MC's like a pound of bacon"
    output = single_byte_xor_cipher(test_input)
    assert output == test_output

if __name__ == '__main__':
    main()
