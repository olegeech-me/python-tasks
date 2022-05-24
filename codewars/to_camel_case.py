"""
Complete the method/function so that it converts dash/underscore delimited words
into camel casing. The first word within the output should be capitalized only if
the original word was capitalized (known as Upper Camel Case, also often referred
to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

import re


def to_camel_case(text):
    words = re.split(r"[-_]", text)
    return words[0] + "".join(w.capitalize() for w in words[1:])


print(to_camel_case("the-stealth-warrior"))

# !!! BETTER DECISION WITH USING MATCH and upper() !!!
# This is how I wanted it to be in the first place:
def to_camel_case_better(text):
    return re.sub("[_-](.)", lambda x: x.group(1).upper(), text)


print(to_camel_case_better("the-stealth-warrior"))
