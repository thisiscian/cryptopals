#/usr/bin/python
# cryptopals crypto challenges
# Set 1: Basics
# - Challenge #7: AES in ECB mode
#   see https://cryptopals.com/sets/1/challenges/7
#
# this problem breaks my hopes of not using external libraries, as we need to
# install pycrypto to be able to easily decrypt AES
#

import base64
from Crypto.Cipher import AES

def main(b64_string: str, key: str) -> str:
    aes_string = base64.b64decode(b64_string)
    aes = AES.new(key)
    return aes.decrypt(aes_string).decode()

if __name__ == "__main__":
    main()
