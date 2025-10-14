import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

"""Тесты для проверки работы функций алгоритма шифра Виженера"""
class VigenereCipherTestCase(unittest.TestCase):

    def test_encrypt_lasts(self):
        self.assertEqual(encrypt_vigenere("XYZ", "ABC"), "XZB")

    def test_encrypt_uppercase(self):
        self.assertEqual(encrypt_vigenere("VINEGERE", "VINEGERE"), "QQAIMIII")

    def test_encrypt_lowercase(self):
        self.assertEqual(encrypt_vigenere("abcdefg", "gfedcba"), "ggggggg")

    def test_encrypt_empty(self):
        self.assertEqual(encrypt_vigenere("", ""), "")

    def test_encrypt_with_special(self):
        with self.assertRaises(ValueError):
            encrypt_vigenere("VINEGERE", "A@B")
        
    def test_decrypt_lasts(self):
        self.assertEqual(decrypt_vigenere("XZB", "ABC"), "XYZ")

    def test_decrypt_uppercase(self):
        self.assertEqual(decrypt_vigenere("QQAIMIII", "VINEGERE"), "VINEGERE")

    def test_decrypt_lowercase(self):
        self.assertEqual(decrypt_vigenere("ggggggg", "gfedcba"), "abcdefg")

    def test_decrypt_empty(self):
        self.assertEqual(decrypt_vigenere("", ""), "")
    
    def test_decrypt_with_special(self):
        with self.assertRaises(ValueError):
            decrypt_vigenere("VINEGERE", "A@B")


if __name__ == "__main__":
    unittest.main()
