import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar

"""Тесты для проверки работы функций алгоритма шифра Цезаря"""
class CaesarCipherTestCase(unittest.TestCase):

    def test_encrypt_lasts(self):
        self.assertEqual(encrypt_caesar("XYZ"), "ABC")

    def test_encrypt_uppercase(self):
        self.assertEqual(encrypt_caesar("CAESAR"), "FDHVDU")

    def test_encrypt_lowercase(self):
        self.assertEqual(encrypt_caesar("abcdefg"), "defghij")

    def test_encrypt_mixed(self):
        self.assertEqual(encrypt_caesar("s-ewfj257kAe..@ru"), "v-hzim257nDh..@ux")

    def test_encrypt_empty(self):
        self.assertEqual(encrypt_caesar(""), "")
        
    def test_decrypt_lasts(self):
        self.assertEqual(decrypt_caesar("ABC"), "XYZ")

    def test_decrypt_uppercase(self):
        self.assertEqual(decrypt_caesar("FDHVDU"), "CAESAR")

    def test_decrypt_lowercase(self):
        self.assertEqual(decrypt_caesar("defghij"), "abcdefg")

    def test_decrypt_mixed(self):
        self.assertEqual(decrypt_caesar("v-hzim257nDh..@ux"), "s-ewfj257kAe..@ru")

    def test_decrypt_empty(self):
        self.assertEqual(decrypt_caesar(""), "")


if __name__ == "__main__":
    unittest.main()
