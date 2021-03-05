import unittest
from ..clear_data import clear_data
from ..data import Data


class TestGetTopKIps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = Data()

    def test_clear_data(self):
        frequencies = {
            "127.0.0.1": {"count": 1, "index_in_heap": 0},
            "127.0.0.2": {"count": 10, "index_in_heap": 1},
            "127.0.0.3": {"count": 100, "index_in_heap": 2},
            "127.0.0.4": {"count": 1000, "index_in_heap": 3},
            "127.0.0.5": {"count": 10000, "index_in_heap": 4},
        }
        top_k_words = [
            (1, "127.0.0.1"),
            (10, "127.0.0.2"),
            (100, "127.0.0.3"),
            (1000, "127.0.0.4"),
            (10000, "127.0.0.5"),
        ]
        self.data.set_frequencies(frequencies)
        self.data.set_top_k_words(top_k_words)
        clear_data()
        self.assertEqual(self.data.get_frequencies(), {})
        self.assertEqual(self.data.get_top_k_words(), [])
