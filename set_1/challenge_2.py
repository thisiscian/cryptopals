#!/usr/bin/python
# fixed xor
# https://cryptopals.com/sets/1/challenges/2


def fixed_xor(hex_a: str, hex_b: str) -> str:
    a = int(hex_a, 16)
    b = int(hex_b, 16)
    c = a ^ b
    return '{:x}'.format(c)


def main():
    test_inputs = [
        '1c0111001f010100061a024b53535009181c',
        '686974207468652062756c6c277320657965'
    ]
    test_output = '746865206b696420646f6e277420706c6179'
    output = fixed_xor(*test_inputs)
    assert output == test_output


if __name__ == '__main__':
    main()
