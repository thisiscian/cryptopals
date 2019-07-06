#!/usr/bin/python

import importlib
import json
import re
import requests
import sys
import traceback
sys.path.insert(0, 'challenges')

test_data = {
    'challenge_1': {
        'inputs': [('49276d206b696c6c696e6720796f757220627261696e206c696b65206'
                    '120706f69736f6e6f7573206d757368726f6f6d')],
        'output': ('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2'
                   'hyb29t')
    },
    'challenge_2': {
        'inputs': ['1c0111001f010100061a024b53535009181c',
                   '686974207468652062756c6c277320657965'],
        'output': '746865206b696420646f6e277420706c6179'
    },
    'challenge_3': {
        'inputs': [('1b37373331363f78151b7f2b783431333d78397828372d363c783'
                        '73e783a393b3736')],
        'outputs': "Cooking MC's like a pound of bacon"
    },
    'challenge_4': {
        'inputs': [requests.get('https://cryptopals.com/static/challenge-data/'
                                '4.txt').text],
        'outputs': "Now that the party is jumping\n"
    },
    'challenge_5': {
        'inputs': [("Burning 'em, if you ain't quick and nimble\nI go crazy "
                    "when I hear a cymbal"),
                   'ICE'],
        'outputs': ('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2'
                     'a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2'
                     '027630c692b20283165286326302e27282f')
    }
}

def run_test(test_name):
    try:
        data = test_data[test_name]
    except KeyError:
        raise Exception('Test not implemented')
    challenge_module = importlib.import_module(test_name)

    output = challenge_module.main(*data['inputs'])

    assert output == data['output']

def test_challenge_5():
    import challenge_5

    assert output == test_output


def main(*challenge_ids):
    '''Run test suite, or specific test if a challenge number is supplied'''
    with open('cryptopals.json') as fh:
        cryptopals_json = json.load(fh)

    for set_dict in cryptopals_json['sets'].values():
        for challenge_id, data in set_dict['challenges'].items():
            if challenge_ids and challenge_id not in challenge_ids:
                continue

            print('\x1b[1mChallenge #{}:\x1b[0m'
                  '\x1b[33m{}\x1b[0m'.format(challenge_id, data['title']))
            try:
                run_test('challenge_{}'.format(challenge_id))
                print('    \x1b[32;1mPASSED\x1b[0m')
            except Exception as e:
                print('    \x1b[31;1mFAILED\x1b[0m:', e)
                if challenge_ids:
                    tb = traceback.format_exc()
                    print(re.sub('^', '        ', tb, flags=re.MULTILINE))

if __name__ == '__main__':
    main(*sys.argv[1:])
