"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter
13 letters after it in the lowercase. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be
returned as they are. Only letters from the latin/english lowercase should be shifted,
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

import string


def rot13(message):
    lowercase = string.ascii_lowercase
    count = len(lowercase)
    result = []
    for s in message:
        if s not in string.ascii_letters:
            result.append(s)
            continue
        upper = s.isupper()
        pos = lowercase.index(s.lower())
        coded_s = lowercase[pos + 13] if pos + 13 < count else lowercase[13 - (count - pos)]
        result.append(coded_s.upper() if upper else coded_s)

    return "".join(result)


print(rot13("test"))  # grfg
print(rot13("Test"))  # Grfg
print(rot13("many"))  # znal
print(rot13("2 of 'em"))  # 2 bs 'rz
