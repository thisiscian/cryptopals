#!/usr/bin/python
from importlib import import_module

set_format = 'https://cryptopals.com/sets/{}'
challenge_format = 'https://cryptopals.com/sets/{}/challenges/{}'

sets= [
    [ 'Convert hex to base64',
      'Fixed XOR',
      'Single-byte XOR cipher',
      'Detect single-character XOR',
      'Implement repeating-key XOR',
      'Break repeating-key XOR',
      'AES in ECB mode',
      'Detect AES in ECB mode'
    ], [
        "Implement PKCS#7 padding",
        "Implement CBC mode",
        "An ECB/CBC detection oracle",
        "Byte-at-a-time ECB decryption (Simple)",
        "ECB cut-and-paste",
        "Byte-at-a-time ECB decryption (Harder)",
        "PKCS#7 padding validation",
        "CBC bitflipping attacks",
    ], [
        "The CBC padding oracle",
        "Implement CTR, the stream cipher mode",
        "Break fixed-nonce CTR mode using substitutions",
        "Break fixed-nonce CTR statistically",
        "Implement the MT19937 Mersenne Twister RNG",
        "Crack an MT19937 seed",
        "Clone an MT19937 RNG from its output",
        "Create the MT19937 stream cipher and break it",
    ],[
        'Break "random access read/write" AES CTR',
        "CTR bitflipping",
        "Recover the key from CBC with IV=Key",
        "Implement a SHA-1 keyed MAC",
        "Break a SHA-1 keyed MAC using length extension",
        "Break an MD4 keyed MAC using length extension",
        "Implement and break HMAC-SHA1 with an artificial timing leak",
        "Break HMAC-SHA1 with a slightly less artificial timing leak",
    ], [
        "Implement Diffie-Hellman",
        "Implement a MITM key-fixing attack on Diffie-Hellman with parameter injection",
        'Implement DH with negotiated groups, and break with malicious "g" parameters',
        "Implement Secure Remote Password (SRP)",
        "Break SRP with a zero key",
        "Offline dictionary attack on simplified SRP",
        "Implement RSA",
        "Implement an E=3 RSA Broadcast attack",
    ], [
        "Implement unpadded message recovery oracle",
        "Bleichenbacher's e=3 RSA Attack",
        "DSA key recovery from nonce",
        "DSA nonce recovery from repeated nonce",
        "DSA parameter tampering",
        "RSA parity oracle",
        "Bleichenbacher's PKCS 1.5 Padding Oracle (Simple Case)",
        "Bleichenbacher's PKCS 1.5 Padding Oracle (Complete Case)",
    ], [
        "CBC-MAC Message Forgery",
        "Hashing with CBC-MAC",
        "Compression Ratio Side-Channel Attacks",
        "Iterated Hash Function Multicollisions",
        "Kelsey and Schneier's Expandable Messages",
        "Kelsey and Kohno's Nostradamus Attack",
        "MD4 Collisions",
        "RC4 Single-Byte Biases",
    ], [
        "Diffie-Hellman Revisited: Small Subgroup Confinement",
        "Pollard's Method for Catching Kangaroos",
        "Elliptic Curve Diffie-Hellman and Invalid-Curve Attacks",
        "Single-Coordinate Ladders and Insecure Twists",
        "Duplicate-Signature Key Selection in ECDSA (and RSA)",
        "Key-Recovery Attacks on ECDSA with Biased Nonces",
        "Key-Recovery Attacks on GCM with Repeated Nonces",
        "Key-Recovery Attacks on GCM with a Truncated MAC",
    ]
]

def get_sets():
    for i, challenges  in enumerate(sets):
        set_name = 'set_{}'.format(i + 1)
        try:
            m = import_module(set_name)
            yield set_name, m, challenges
        except ModuleNotFoundError:
            yield set_name, None, challenges

def get_challenges(set_name, module, challenges):
    for i, name in enumerate(challenges):
        challenge = '{}.challenge_{}'.format(set_name, i + 1)
        try:
            m = import_module(challenge, module)
            yield name, m
        except ModuleNotFoundError:
            yield name, None

def get_progress():
    output = []
    for set_name, set_module, challenges in get_sets():
        if set_module is None:
            output.append([None] * len(challenges))
        else:
            set_output = []
            for challenge_name, challenge_module in get_challenges(set_name, set_module, challenges):
                if challenge_module is None:
                    set_output.append(None)
                else:
                    try:
                        challenge_module.main()
                        set_output.append(True)
                    except AssertionError:
                        set_output.append(False)
            output.append(set_output)
    return output

def main():
    progress = get_progress()
    print('# Cryptopals progress')
    print('solutions to [Cryptopal](https://cryptopals.com) problems')
    for i, challenges in enumerate(progress):
        I = i + 1
        print('- [Set {}]({})'.format(I, set_format.format(I)))
        for j, status in enumerate(challenges):
            print('  - [{}] [{}]({})'.format('X' if status else ' ',
                                             sets[i][j],
                                             challenge_format.format(I, j + 1)))

if __name__ == '__main__':
    main()
