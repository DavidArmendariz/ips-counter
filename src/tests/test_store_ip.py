import unittest
import json
from ..store_ip import store_ip
from ..data import Data


class TestStoreIp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = Data()

    def setUp(self):
        self.data.set_frequencies({})
        self.data.set_top_k_words([])

    def test_store_ip(self):
        ips = (
            ["127.0.0.1"] * 100
            + ["127.0.0.2"] * 60
            + ["127.0.0.3"] * 120
            + ["127.0.0.4"] * 50
            + ["127.0.0.5"] * 70
        )
        for ip in ips:
            store_ip(ip)
        expectedFrequencies = {
            "127.0.0.1": {"count": 100, "index_in_heap": 3},
            "127.0.0.2": {"count": 60, "index_in_heap": 1},
            "127.0.0.3": {"count": 120, "index_in_heap": 2},
            "127.0.0.4": {"count": 50, "index_in_heap": 0},
            "127.0.0.5": {"count": 70, "index_in_heap": 4},
        }
        expectedMinHeap = [
            (50, "127.0.0.4"),
            (60, "127.0.0.2"),
            (120, "127.0.0.3"),
            (100, "127.0.0.1"),
            (70, "127.0.0.5"),
        ]
        self.assertEqual(self.data.get_frequencies(), expectedFrequencies)
        self.assertEqual(self.data.get_top_k_words(), expectedMinHeap)
