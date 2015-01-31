# __author__ = 'dkf'
#-*- coding:utf-8 -*-
#IDE：Pycharm3.4.1
import string,re


charToSoundex = {"A": "9",
                 "B": "1",
                 "C": "2",
                 "D": "3",
                 "E": "9",
                 "F": "1",
                 "G": "2",
                 "H": "9",
                 "I": "9",
                 "J": "2",
                 "K": "2",
                 "L": "4",
                 "M": "5",
                 "N": "5",
                 "O": "9",
                 "P": "1",
                 "Q": "2",
                 "R": "6",
                 "S": "2",
                 "T": "3",
                 "U": "9",
                 "V": "1",
                 "W": "9",
                 "X": "2",
                 "Y": "9",
                 "Z": "2"}

allChar = string.uppercase + string.lowercase
charToSoundex = string.maketrans(allChar, "91239129922455912623919292" * 2)


def soundex(source):
    """convert string to Soundex equivalent"""
    #allChars = string.uppercase + string.lowercase
    # if not re.search('^[A-Za-z]+$', source):
    #     return "0000"
    if (not source) and (not source.isalpha()):
        return "0000"
    #Soundex algorithm:
    #1. make first charter uppercase
    digits = source[0].upper() + source[1:].translate(charToSoundex)
    #3. remove consecutive duplicates
    digits2 = digits[0]
    for d in digits[1:]:
        if digits2[-1] != d:
            digits2 += d
    return (digits2.replace('9', '') + '0000')[:4]


if __name__ == "__main__":
    from timeit import Timer
    names = ('Pilgrim', 'flingjingwaller')
    for name in names:
        statement = "soundex('%s')" % name
        t = Timer(statement, "from __main__ import soundex")
        print name.ljust(15), soundex(name), min(t.repeat())



























