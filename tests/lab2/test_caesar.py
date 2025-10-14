"""Тесты для проверки работы функций алгоритма шифра Цезаря"""
import unittest

from src.lab2.caesar import decrypt_caesar, encrypt_caesar


class CaesarCipherTestCase(unittest.TestCase):
    def test_encrypt_lasts(self):
        """Проверка шифрования крайних букв"""
        self.assertEqual(encrypt_caesar("XYZ"), "ABC")

    def test_encrypt_uppercase(self):
        """Проверка шифрования заглавных букв"""
        self.assertEqual(encrypt_caesar("CAESAR"), "FDHVDU")

    def test_encrypt_lowercase(self):
        """Проверка шифрования незаглавных букв"""
        self.assertEqual(encrypt_caesar("abcdefg"), "defghij")

    def test_encrypt_mixed(self):
        """Проверка шифрования смешанной строки"""
        self.assertEqual(encrypt_caesar("s-ewfj257kAe..@ru"), "v-hzim257nDh..@ux")

    def test_encrypt_empty(self):
        """Проверка шифрования пустой строки"""
        self.assertEqual(encrypt_caesar(""), "")

    def test_decrypt_lasts(self):
        """Проверка расшифровывания крайних букв"""
        self.assertEqual(decrypt_caesar("ABC"), "XYZ")

    def test_decrypt_uppercase(self):
        """Проверка расшифровывания заглавных букв"""
        self.assertEqual(decrypt_caesar("FDHVDU"), "CAESAR")

    def test_decrypt_lowercase(self):
        """Проверка расшифровывания незаглавных букв"""
        self.assertEqual(decrypt_caesar("defghij"), "abcdefg")

    def test_decrypt_mixed(self):
        """Проверка расшифровывания смешанной строки"""
        self.assertEqual(decrypt_caesar("v-hzim257nDh..@ux"), "s-ewfj257kAe..@ru")

    def test_decrypt_empty(self):
        """Проверка расшифровывания пустой строки"""
        self.assertEqual(decrypt_caesar(""), "")


if __name__ == "__main__":
    unittest.main()
