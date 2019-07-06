#!/usr/bin/python
# break repeating-key xor
# https://cryptopals.com/sets/1/challenges/6

from base64 import b64decode
import requests
from .challenge_3 import decode_single_xor
from .generate_frequencies import score_string


def hamming_dist(a: bytes, b: bytes):
    c_bytes = bytes(A ^ B for A, B in zip(a, b))
    counts = sum(bin(x).count("1") for x in c_bytes)
    return counts


def chunk(a, size: int):
    for i in range(0, len(a), size):
        yield a[i:i+size]

def get_pairs(iterable):
    while True:
        try:
            a = next(iterable)
            b = next(iterable)
            yield a, b
        except StopIteration:
            return


def break_repeating_key_xor(string: str) -> str:
    str_bytes = b64decode(string)
    keysizes = []

    l = 6
    for keysize in range(2, 40):
        count = 0
        dist = 0
        for a, b in get_pairs(chunk(str_bytes, keysize)):
            count += 1
            dist += hamming_dist(a, b)

        if count == 0:
            continue

        dist /= count
        keysizes.append((keysize, dist))

    keysizes.sort(key = lambda v: v[1])
    keysizes = [k[0] for k in keysizes]
    best_score = None
    best_output = None

    for keysize in keysizes[:3]:
        for i in range(keysize):
            sub_bytes = str_bytes[i::keysize]
            sub_string = sub_bytes.hex()
            output = []
            try:
                solve, best = decode_single_xor(sub_string)
                output.append(solve)
            except ValueError as e:
                break

            true_output = ''.join([''.join(a) for a in zip(*output)])
            score = score_string(true_output)
            if best_score is None or score > best_score:
                best_score = score
                best_output = true_output
                print(keysize, score, '!!!', true_output[:15])

    return best_output

def main():
    test_inputs_1 = [b'this is a test', b'wokka wokka!!!']
    test_output = 37

    output = hamming_dist(*test_inputs_1)
    assert output == test_output

    test_input_2 = requests.get('https://cryptopals.com/static/challenge-data/'
                                '6.txt').text

    test_output = ''
    output = break_repeating_key_xor(test_input_2)
    print(output)
    assert output == test_output

if __name__ == '__main__':
    main()
