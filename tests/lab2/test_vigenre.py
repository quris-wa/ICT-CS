"""Тесты для проверки работы функций алгоритма шифра Виженера"""
import unittest

from src.lab2.vigenre import decrypt_vigenere, encrypt_vigenere


class VigenereCipherTestCase(unittest.TestCase):
    def test_encrypt_lasts(self):
        """Проверка шифрования крайних букв"""
        self.assertEqual(encrypt_vigenere("XYZ", "ABC"), "XZB")

    def test_encrypt_uppercase(self):
        """Проверка шифрования заглавных букв"""
        self.assertEqual(encrypt_vigenere("VINEGERE", "VINEGERE"), "QQAIMIII")

    def test_encrypt_lowercase(self):
        """Проверка шифрования незаглавных букв"""
        self.assertEqual(encrypt_vigenere("abcdefg", "gfedcba"), "ggggggg")

    def test_encrypt_empty(self):
        """Проверка шифрования пустой строки"""
        self.assertEqual(encrypt_vigenere("", ""), "")

    def test_encrypt_with_special(self):
        """Проверка шифрования с ключом со специальным символом"""
        with self.assertRaises(ValueError):
            encrypt_vigenere("VINEGERE", "A@B")

    def test_decrypt_lasts(self):
        """Проверка расшифровывания крайних букв"""
        self.assertEqual(decrypt_vigenere("XZB", "ABC"), "XYZ")

    def test_decrypt_uppercase(self):
        """Проверка расшифровывания заглавных букв"""
        self.assertEqual(decrypt_vigenere("QQAIMIII", "VINEGERE"), "VINEGERE")

    def test_decrypt_lowercase(self):
        """Проверка расшифровывания незаглавных букв"""
        self.assertEqual(decrypt_vigenere("ggggggg", "gfedcba"), "abcdefg")

    def test_decrypt_empty(self):
        """Проверка расшифровывания пустой строки"""
        self.assertEqual(decrypt_vigenere("", ""), "")

    def test_decrypt_with_special(self):
        """Проверка расшифровывания с ключом со специальным символом"""
        with self.assertRaises(ValueError):
            decrypt_vigenere("VINEGERE", "A@B")


if __name__ == "__main__":
    unittest.main()
