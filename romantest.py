# __author__ = 'dkf'
#-*- coding:utf-8 -*-
#IDE：Pycharm3.4.1

import roman
import unittest


class KnownValues(unittest.TestCase):
    knownValues = ((1, 'I'),
                   (2, 'II'),
                   (3, 'III'),
                   (4, 'Iv'),
                   (5, 'V'),
                   (6, 'VI'),
                   (7, 'VII'),
                   (8, 'VIII'),
                   (9, 'IX'),
                   (10, 'X'),
                   (50, 'L'),
                   (100, 'C'),
                   (500, 'D'),
                   (1000, 'M'),
                   (31, 'XXXI'),
                   (3888, 'MMMDCCCLXXXVIII'),
                   (3940, 'MMMCMXL'))

    def testToRomanKnownValues(self):
        """toRoman should give known result with konwn input"""
        for integer, numeral in self.knownValues:
            result = roman.toRoman(integer)
            self.assertEqual(numeral, result)

    def testFromRomanKnownValues(self):
        """fromRoman should give known result with known input"""
        for integer, numeral in self.knownValues:
            result = roman.fromRoman(numeral)
            self.assertEqual(integer, result)


class ToRomanBadInput(unittest.TestCase):
    def testTooLarge(self):
        """toRoman should fail with large input"""
        self.assertRaises(roman.OutOfRangeError, roman.roRoman, 4000)

    def testZero(self):
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 0)

    def testNegative(self):
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, -1)

    def testNonInteger(self):
        self.assertRaises(roman.NotIntegerError, roman.toRoman, 0.5)


class FromRomanBadInput(unittest.TestCase):
    def testTOOManyRepeatedNumerrals(self):
        for s in ('MMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

    def testRepeatedPairs(self):
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IXIX'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

    def testMalformedAntecedent(self):
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX',
                    'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

    def testBlank(self):
        self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, "")


class SanityCheck(unittest.TestCase):
    def testSanity(self):
        for integer in range(1, 4000):
            numeral = roman.toRoman(integer)
            result = roman.fromRoman(numeral)
            self.assertEqual(integer, result)


class CaseCheck(unittest.TestCase):
    def testToRomanCase(self):
        for integer in range(1, 4000):
            numeral = roman.toRoman(integer)
            self.assertEqual(numeral, numeral.upper())

    def testFromRomanCase(self):
        for integer in range(1, 4000):
            numeral = roman.toRoman(integer)
            roman.fromRoman(numeral.upper())
            self.assertRaises(roman.InvalidRomanNumeralError,
                              roman.fromRoman, numeral.lower())

if __name__ == "__main__":
    unittest.main()

























