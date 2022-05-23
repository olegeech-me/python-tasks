"""
Create two functions to encode and then decode a string using the Rail Fence Cipher.
This cipher is used to encode a string by placing each character successively in a
diagonal along a set of "rails". First start off moving diagonally and down.
When you reach the bottom, reverse direction and move diagonally and up until you reach
the top rail. Continue until you reach the end of the string. Each "rail" is then read
left to right to derive the encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three
rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    
The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN
Write a function/method that takes 2 arguments, a string and the number of rails,
and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the
number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an
empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity.
There are, however, tests that include punctuation. Don't filter out punctuation as
they are a part of the string.
"""


def encode_rail_fence_cipher(string, n):
    input = [s for s in string]
    encoded = [[] for i in range(n)]

    def encode_input(rails_range):
        for i in rails_range:
            print(f"Coding: i={i}, input={input}, encoded={encoded}")
            if input:
                encoded[i].append(input.pop(0))
            else:
                break

    while input:
        encode_input(range(0, n, 1))
        encode_input(range(n - 2, 0, -1))

    return "".join(w for s in encoded for w in s)


def decode_rail_fence_cipher(string, n):
    input = [s for s in string]
    decode_map = [0 for x in range(n)]
    mapped = [[] for i in range(n)]
    decoded = []

    def map_input(rails_range):
        for i in rails_range:
            print(f"Mapping: i={i}, input={input}, decode_map={decode_map}")
            if input:
                del input[0]
                decode_map[i] += 1
            else:
                break

    def decode_mapped(rails_range):
        for i in rails_range:
            print(f"Decoding: i={i}, mapped={mapped}, decoded={decoded}")
            if mapped[i]:
                decoded.append(mapped[i].pop(0))
            else:
                break

    while input:
        map_input(range(0, n, 1))
        map_input(range(n - 2, 0, -1))

    input = [s for s in string]
    for i in range(n):
        mapped[i] = [input.pop(0) for j in range(decode_map[i])]

    while [b for a in mapped for b in a]:
        decode_mapped(range(0, n, 1))
        decode_mapped(range(n - 2, 0, -1))

    return "".join(w for s in decoded for w in s)


print(encode_rail_fence_cipher("obfuscation", 5))
print(decode_rail_fence_cipher("osibuctofan", 3))
print(decode_rail_fence_cipher("oibtofanucs", 5))
