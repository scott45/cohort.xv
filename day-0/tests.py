import unittest
from prime import is_prime_number

# simple tests to check expected and unexpected prime numbers


class Prime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime_number(2))

    def test_3_is_prime(self):
        self.assertTrue(is_prime_number(3))

    def test_5_is_prime(self):
        self.assertTrue(is_prime_number(5))

    def test_7_is_prime(self):
        self.assertTrue(is_prime_number(7))

    def test_11_is_prime(self):
        self.assertTrue(is_prime_number(11))

    def test_13_is_prime(self):
        self.assertTrue(is_prime_number(13))

    def test_17_is_prime(self):
        self.assertTrue(is_prime_number(17))

    def test_6_is_not_prime(self):
        self.assertFalse(is_prime_number(6))

    def test_9_is_not_prime(self):
        self.assertFalse(is_prime_number(9))

    def test_25_is_not_prime(self):
        self.assertFalse(is_prime_number(25))
