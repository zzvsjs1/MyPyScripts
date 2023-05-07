import hashlib

ipad = 0x36363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636
opad = 0x5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c


def string_to_hex(string: str) -> str:
    hex_string = ""
    for char in string:
        hex_string += hex(ord(char))[2:].zfill(2)
    return hex_string


def fill_zero(in_str: str) -> str:
    zero = 128
    while len(in_str) != zero:
        in_str += '0'
    assert len(in_str) == zero
    return in_str


def hash_to(k: str, m: str) -> str:
    ascii_k = fill_zero(string_to_hex(k))
