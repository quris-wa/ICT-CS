import unittest
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt

"""Тесты для функций RSA"""
class TestRSA(unittest.TestCase):

    """Проверка is_prime()"""
    def test_is_prime_true(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(97))

    def test_is_prime_false(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(100))

    """Проверка gcd()"""
    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)
        self.assertEqual(gcd(100, 10), 10)

    """Проверка multiplicative_inverse()"""
    def test_multiplicative_inverse_exists(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_multiplicative_inverse_not_exists(self):
        with self.assertRaises(ValueError):
            multiplicative_inverse(6, 42)

    """Проверка generate_keypair()"""
    def test_generate_keypair_primes(self):
        public, private = generate_keypair(17, 23)
        e, n1 = public
        d, n2 = private
        self.assertEqual(n1, n2)
        self.assertTrue(isinstance(e, int) and isinstance(d, int))
        self.assertTrue(e < (17 - 1) * (23 - 1))
        self.assertTrue(d < (17 - 1) * (23 - 1))

    def test_generate_keypair_invalid(self):
        with self.assertRaises(ValueError):
            generate_keypair(15, 15)
        with self.assertRaises(ValueError):
            generate_keypair(8, 9)

    """Проверка encrypt() и decrypt()"""
    def test_encrypt_and_decrypt(self):
        public, private = generate_keypair(17, 23)
        msg = "HELLO"
        encrypted = encrypt(public, msg)
        decrypted = decrypt(private, encrypted)
        self.assertEqual(decrypted, msg)

if __name__ == "__main__":
    unittest.main()
