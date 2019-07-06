'''Utilities path for cryptopals'''
import base64
import binascii
import math
import requests
import string
from collections import Counter

shakespeare = requests.get('https://ocw.mit.edu/ans7870/6/6.006/s08/'
                           'lecturenotes/files/t8.shakespeare.txt').text
eng_freq = Counter(shakespeare)


class XOR:
    @classmethod
    def auto(self, a, b):
        bytes_a = BytesConverter.auto(a)
        bytes_b = BytesConverter.auto(b)

        a_len = len(bytes_a)
        b_len = len(bytes_b)

        if b_len > 0 and a_len > b_len:
            mult = math.ceil(a_len / b_len)
            bytes_b = bytes_b * mult
            bytes_b = bytes_b[:a_len]

        elif a_len != 0 and b_len > a_len:
            mult = math.ceil(b_len / a_len)
            bytes_a = bytes_a * mult
            bytes_a = bytes_a[:b_len]

        return bytes(A ^ B for A, B in zip(bytes_a, bytes_b))

    @classmethod
    def toString(cls, a, b):
        xor_bytes = cls.auto(a, b)
        return BytesConverter.toString(xor_bytes)


class Base64Converter:
    @classmethod
    def toBytes(cls, b64_string: str) -> bytes:
        return base64.b64decode(b64_string)

    @classmethod
    def toHexString(cls, b64_string: str) -> str:
        return cls.toBytes(b64_string).hex()


class HexStringConverter:
    @classmethod
    def toBytes(cls, hex_string: str) -> str:
        return bytes.fromhex(hex_string)

    @classmethod
    def toBase64(cls, hex_string: str) -> str:
        hex_bytes = cls.toBytes(hex_string)
        return base64.b64encode(hex_bytes).decode()


class StringConverter:
    @classmethod
    def toHexString(cls, string: str) -> bytes:
        return ByteConverter.toHexString((cls.toBytes(string)))

    @classmethod
    def toBytes(cls, string: str) -> bytes:
        return string.encode()


class BytesConverter:
    @classmethod
    def auto(cls, item):
        if isinstance(item, bytes):
            return item
        elif isinstance(item, str):
            try:
                return bytes.fromhex(item)
            except ValueError:
                pass

            try:
                return base64.b64decode(item)
            except binascii.Error:
                pass

            return item.encode()
        raise Exception('Failed to find type')

    @classmethod
    def toHexString(cls, byte) -> str:
        return byte.hex()

    @classmethod
    def toBase64(cls, byte) -> str:
        return base64.b64encode(string).decode()

    @classmethod
    def toString(cls, byte) -> str:
        return byte.decode()

def xor_hex_strings(hex_string_a: str, hex_string_b: str) -> str:
    a_len = len(hex_string_a)
    b_len = len(hex_string_b)

    if a_len > b_len:
        mult = math.ceil(a_len / b_len)
        hex_string_b = hex_string_b * mult
        hex_string_b = hex_string_b[:a_len]

    elif b_len > a_len:
        mult = math.ceil(b_len / a_len)
        hex_string_a = hex_string_a * mult
        hex_string_a = hex_string_a[:b_len]

    a_bytes = HexStringConverter.toBytes(hex_string_a)
    b_bytes = HexStringConverter.toBytes(hex_string_b)

    c_bytes = bytes(A ^ B for A, B in zip(a_bytes, b_bytes))

    return BytesConverter.toHexString(c_bytes)

def guess_decode_single_character_xor(s: str) -> str:
    best_score = None
    best_character = None
    output = None
    for c in string.printable:
        try:
            xor_string = XOR.toString(s, c)
            score = score_string(xor_string)

            if best_score is None or best_score < score:
                best_score = score
                best_character = c
                output = xor_string

        except UnicodeDecodeError:
            continue

    return best_score, best_character, output

def score_string(string: str) -> float:
    a = eng_freq
    b = Counter(string)
    shared_keys = set(a.keys()).intersection(set(b.keys()))
    top = sum([a[k] * b[k] for k in shared_keys])
    bottom = (math.sqrt(sum([v * v for v in a.values()])) *
              math.sqrt(sum([v * v for v in b.values()])))

    if bottom == 0:
        return 0

    v = top / bottom
    return v
