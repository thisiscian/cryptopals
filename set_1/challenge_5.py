#!/usr/bin/python
# implement repeating-key XORG
# https://cryptopals.com/sets/1/challenges/5

from .. import util

def repeating_key_xor(string: str, key: str) -> str:
    encoding = 'utf-8'
    str_bytes = bytes(string, encoding)
    key_bytes = bytes(key, encoding)
    l = len(key_bytes)

    xor_bytes = bytes(b ^ key_bytes[i % l] for i, b in enumerate(str_bytes))
    return util.BytesConverter.toHexString(xor_bytes)

def main():
    test_inputs = [
        ("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear "
        "a cymbal"),
        'ICE'
    ]

    test_output = ('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a'
                   '26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027'
                   '630c692b20283165286326302e27282f')
    output = repeating_key_xor(*test_inputs)
    assert output == test_output

if __name__ == '__main__':
    main()
    
