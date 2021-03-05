import unittest
from ..data import Data


class TestDataClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = Data()

    def test_frequencies(self):
        frequencies = {"127.0.0.1": {"count": 1, "index_in_heap": 2}}
        self.data.set_frequencies(frequencies)
        self.assertEqual(frequencies, self.data.get_frequencies())

    def test_top_k_words(self):
        top_k_words = [(2, "127.0.0.1"), (3, "192.168.10.1")]
        self.data.set_top_k_words(top_k_words)
        self.assertEqual(top_k_words, self.data.get_top_k_words())
