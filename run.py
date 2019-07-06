#!/usr/bin/python
import argparse
import json
import re
import requests
from html.parser import HTMLParser
from importlib import import_module

cryptopals_json = {
    'base_url': 'https://cryptopals.com',
    'sets': {}
}
challenges = []

class CryptoPalsHTMLParser(HTMLParser):
    set_id = None
    challenge_id = None
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            set_match = re.match('/sets/(\d+)$', value)
            challenge_match = re.match('/sets/(\d+)/challenges/(\d+)$', value)
            if key == 'href' and set_match:
                self.set_id = int(set_match.group(1))
                if self.set_id in cryptopals_json['sets']:
                    self.set_id = None
                    continue
                print('set', self.set_id, value)
                cryptopals_json['sets'][self.set_id] = {
                    'url': value,
                    'title': None,
                    'completion': None,
                    'challenges': {}
                }
            elif key == 'href' and challenge_match:
                self.set_id = int(challenge_match.group(1))
                self.challenge_id = int(challenge_match.group(2))
                print('set', self.set_id, 'challenge', self.challenge_id)
                cryptopals_json['sets'][self.set_id]['challenges'][self.challenge_id] = {
                    'url': value,
                    'title': None,
                    'completed': None,
                }

                self.do_handle_challenge = True
                challenges.append([value])

    def handle_data(self, data):
        if self.set_id is not None and self.challenge_id is not None:
            cryptopals_json['sets'][self.set_id]['challenges'][self.challenge_id]['title'] = data
        elif self.set_id is not None:
            cryptopals_json['sets'][self.set_id]['title'] = data

    def handle_endtag(self, tag):
        set_id = self.set_id
        challenge_id = self.challenge_id
        self.set_id = None
        self.challenge_id = None

        if set_id is not None and challenge_id is None:
            set_url = cryptopals_json['sets'][set_id]['url']
            url = cryptopals_json['base_url'] + set_url
            
            response = requests.get(url)
            self.feed(response.text)

html_parser = CryptoPalsHTMLParser()
response = requests.get(cryptopals_json['base_url'])
try:
    html_parser.feed(response.text)
except AssertionError:
    pass

for set_json in cryptopals_json['sets']:
    print(set_json)
    
print(cryptopals_json)

exit(1)



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

def update_readme():
    with open('README.md', 'w') as fh:
        progress = get_progress()
        fh.write('# Cryptopals progress\n')
        fh.write('solutions to [Cryptopal](https://cryptopals.com) problems\n')
        for i, challenges in enumerate(progress):
            I = i + 1
            fh.write('- [Set {}]({})\n'.format(I, set_format.format(I)))
            for j, status in enumerate(challenges):
                J = j + 1
                title = sets[i][j]
                challenge_url = challenge_format.format(I, J)
                fh.write('  - [{}] [{}]({})'.format('X' if status else ' ',
                                                    title,
                                                    challenge_url))

def main():
    pass

if __name__ == '__main__':
    update_readme()
