"""Тесты для функций RSA"""
import unittest

from src.lab2.rsa import decrypt, encrypt, gcd, generate_keypair, is_prime, multiplicative_inverse


class TestRSA(unittest.TestCase):

    def test_is_prime_true(self):
        """Проверка is_prime() на возврат true"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(97))

    def test_is_prime_false(self):
        """Проверка is_prime() на возврат false"""
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(100))

    def test_gcd(self):
        """Проверка работы gcd()"""
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)
        self.assertEqual(gcd(100, 10), 10)

    def test_multiplicative_inverse_exists(self):
        """Проверка работы multiplicative_inverse()"""
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_multiplicative_inverse_not_exists(self):
        """Проверка работы multiplicative_inverse() на несуществование"""
        with self.assertRaises(ValueError):
            multiplicative_inverse(6, 42)

    def test_generate_keypair_primes(self):
        """Проверка работы generate_keypair()"""
        public, private = generate_keypair(17, 23)
        e, n1 = public
        d, n2 = private
        self.assertEqual(n1, n2)
        self.assertTrue(isinstance(e, int) and isinstance(d, int))
        self.assertTrue(e < (17 - 1) * (23 - 1))
        self.assertTrue(d < (17 - 1) * (23 - 1))

    def test_generate_keypair_invalid(self):
        """Проверка работы generate_keypair() на некорректных значениях"""
        with self.assertRaises(ValueError):
            generate_keypair(15, 15)
        with self.assertRaises(ValueError):
            generate_keypair(8, 9)

    def test_encrypt_and_decrypt(self):
        """Проверка encrypt() и decrypt()"""
        public, private = generate_keypair(17, 23)
        msg = "HELLO"
        encrypted = encrypt(public, msg)
        decrypted = decrypt(private, encrypted)
        self.assertEqual(decrypted, msg)


if __name__ == "__main__":
    unittest.main()
