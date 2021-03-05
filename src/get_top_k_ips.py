import heapq
from .data import Data

data = Data()


def get_top_k_ips():
    largest = heapq.nlargest(100, data.get_top_k_words())
    return list(map(lambda node: node[1], largest))