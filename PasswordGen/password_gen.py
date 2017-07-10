#! /usr/bin/python

import string
import random
import sys
import re

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SPECIAL = string.punctuation


def generate_password(length=14, groups='ULD', musts=''):
    assert (length >= 4), "A password of length {} is much too short".format(length)
    assert (re.match('^[ULDSulds]+$', groups) is not None), groups+" contains unrecognized groups"
    assert (len(musts) <= length), "The must have group selection: "+musts+" is longer than the password"
    if len(musts): assert (re.match('^[ULDSulds]+$', musts) is not None), \
        "The must have group selection: "+musts+" contain unrecognized groups"

    # Ensure that the minimum characters from each group are selected
    password = ''
    for selection in musts:
        if selection.upper() == 'U':
            password += random.choice(UPPERCASE)
        elif selection.upper() == 'L':
            password += random.choice(LOWERCASE)
        elif selection.upper() == 'D':
            password += random.choice(DIGITS)
        elif selection.upper() == 'S':
            password += random.choice(SPECIAL)

    # Fill in the remaining length with characters from the chosen groups
    acceptable_groups = set([g for g in groups])
    acceptable = ''
    for g in acceptable_groups:
        if g.upper() == 'U': acceptable += UPPERCASE
        elif g.upper() == 'L': acceptable += LOWERCASE
        elif g.upper() == 'D': acceptable += DIGITS
        elif g.upper() == 'S': acceptable += SPECIAL

    for i in range(length-len(musts)):
        password += random.choice(acceptable)

    # Shuffle the chosen characters and return the final password
    password = [c for c in password]
    random.shuffle(password)
    return ''.join(password)


if __name__ == '__main__':
    assert (len(sys.argv) <= 4), 'Given too many arguments'
    if len(sys.argv) >= 2:
        try: int(sys.argv[1])
        except ValueError: raise AssertionError("{} is not an integer".format(sys.argv[1]))

    if len(sys.argv) == 1:
        print(generate_password())
    elif len(sys.argv) == 2:
        print(generate_password(int(sys.argv[1])))
    elif len(sys.argv) == 3:
        print(generate_password(int(sys.argv[1]), sys.argv[2]))
    else:
        print(generate_password(int(sys.argv[1]), sys.argv[2], sys.argv[3]))
