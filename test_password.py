# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcd"), "abce")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")

    def test_getNextFullZ(self):
        self.assertRaises(pwd.getNext('zz'), ValueError)

    def test_getNextEmpty(self):
        self.assertRaises(pwd.getNext(""), ValueError)

    def test_hasSeries_true(self):
        self.assertTrue(pwd.hasSeries("abcdef"))

    def test_hasSeries_false(self):
        self.assertFalse(pwd.hasSeries("aef"))

    def test_hasTwoPairs_true(self):
        self.assertTrue(pwd.hasTwoPairs('aba'))

    def test_hasTwoPairs_false(self):
        self.assertFalse(pwd.hasTwoPairs('aaa'))

    def test_hasNoBadChar_true(self):
        self.assertTrue(pwd.hasNoBadChar('adbgrd'))

    def test_hasNoBadChar_false(self):
        self.assertFalse(pwd.hasNoBadChar('iol'))
        



# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
