#/usr/bin/python
# cryptopals crypto challenges
# Set 2: Block crypto
# - Challenge #9: Implement PKCS#7 padding
#   see https://cryptopals.com/sets/2/challenges/9

def main(input_string: str, block_size: int) -> str:
    pad = block_size % len(input_string)
    padding = bytes([pad] * pad)
    output = input_string + padding.decode()
    return output

if __name__ == "__main__":
    main("YELLOW SUBMARINE", 20)
