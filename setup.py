#!/usr/bin/python
import json
import os
import re
import requests
from html.parser import HTMLParser

try:
    with open('cryptopals.json') as fh:
        cryptopals_json = json.load(fh)
except:
    with open('cryptopals.json', 'w') as fh:
        fh.write('{"base_url": "https://cryptopals.com", "sets": {}}')

if not cryptopals_json['sets']:
    refresh()

def refresh():
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

    with open('cryptopals.json', 'w') as fh:
        json.dump(cryptopals_json, fh)

def make_challenge(set_id, challenge_id):
    challenge_dir = 'challenges/'
    if not os.path.isdir(challenge_dir):
        os.mkdir(challenge_dir)

    challenge_path = challenge_dir + 'challenge_{}.py'.format(challenge_id)
    if os.path.isfile(challenge_path):
        return

    set_dict = cryptopals_json['sets'][str(set_id)]
    challenge = set_dict['challenges'][str(challenge_id)]
    with open(challenge_path, 'w') as fh:
        fh.write('#/usr/bin/python\n')
        fh.write('# cryptopals crypto challenges\n')
        fh.write('# {}\n'.format(set_dict['title']))
        fh.write('# - Challenge #{}: {}\n'.format(challenge_id,
                                                  challenge['title']))
        fh.write('#   see {}\n\n'.format(cryptopals_json['base_url'] +
                                         challenge['url']))
        fh.write('def main():\n    pass\n\n')
        fh.write('if __name__ == "__main__":\n')
        fh.write('    main()')

def make_challenges():
    for set_id, json_data in cryptopals_json['sets'].items():
        for challenge_id in json_data['challenges'].keys():
            make_challenge(set_id, challenge_id)


make_challenges()
