#!/usr/bin/python
# detecting single-character xor
# https://cryptopals.com/sets/1/challenges/4

import requests
from .. import util

def detect_single_character_xor(string: str) -> str:
    best_score = None
    output = None
    for line in string.splitlines():
        score, char, xor_string = util.guess_decode_single_character_xor(line)
        if score is None:
            continue

        if best_score is None or score > best_score:
            best_score = score
            output = xor_string

    return output

def main():
    response = requests.get('https://cryptopals.com/static/challenge-data/4.txt')
    test_input = response.text
    test_output = "Now that the party is jumping\n"
    output = detect_single_character_xor(test_input)
    assert output == test_output

if __name__ == '__main__':
    m
