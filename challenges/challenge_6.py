#/usr/bin/python
# cryptopals crypto challenges
# Set 1: Basics
# - Challenge #6: Break repeating-key XOR
#   see https://cryptopals.com/sets/1/challenges/6

import base64
from string import printable
from util import hamming_dist, language_score
from itertools import zip_longest

def find_best_keysizes(data, m=2, M=40, average_over=2, output_count = 4):
    keysizes = []
    for keysize in range(m, M):
        dists = []
        for i in range(average_over):
            I = 2 * i
            J = 2 * i + 1
            K = 2 * i + 2
            
            a = data[I * keysize:J * keysize]
            b = data[J * keysize:K * keysize]
            dist = hamming_dist(a, b)
            dists.append(dist)
        avg_dist = sum(dists) / (keysize * average_over)

        keysizes.append((avg_dist, keysize))

    keysizes.sort()
    return [k[1] for k in keysizes[:output_count]] 


def main(b64_file_contents: str) -> str:
    file_contents = base64.b64decode(b64_file_contents)
    
    best_keysizes = find_best_keysizes(file_contents, average_over=8, output_count = 2)

    true_best_score = 0
    true_best_string = None
    for keysize in best_keysizes:
        key = ''
        split_output = []
        for i in range(keysize):
            best_score = 0
            best_xor = None
            best_char = None
            data = file_contents[i::keysize]
            for char in printable:
                try:
                    xor_string = bytes(a ^ ord(char) for a in data).decode()
                except UnicodeDecodeError:
                    ### if we can't decode it, it definitely isn't human readable
                    continue

                score = language_score(xor_string)

                if score > best_score:
                    best_score = score
                    best_xor = xor_string
                    best_char = char
            split_output.append(best_xor)
            key += best_char

        output = ''.join([ ''.join(z) for z in zip_longest(*split_output, fillvalue='')])
        output_score = language_score(output)
        if output_score > true_best_score:
            true_best_score = output_score
            true_best_string = output

    return true_best_string
    

if __name__ == "__main__":
    print(37 == hamming_dist('this is a test'.encode(),
                             'wokka wokka!!!'.encode()))
