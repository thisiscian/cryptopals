#/usr/bin/python
# cryptopals crypto challenges
# Set 1: Basics
# - Challenge #8: Detect AES in ECB mode
#   see https://cryptopals.com/sets/1/challenges/8

from collections import Counter

def main(hex_strings):
    most_dupes = 0
    output = None
    for line in hex_strings.splitlines():
        line_bytes = bytes.fromhex(line)
        dupe_counter = Counter([line_bytes[i:i+16] for i in range(0, len(line_bytes), 16)])
        dupes = sum([ c for b, c in dupe_counter.most_common() if c > 1])
        if dupes > most_dupes:
            most_dupes = dupes
            output = line
    return output


if __name__ == "__main__":
    main()
