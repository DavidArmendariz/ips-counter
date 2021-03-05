import heapq
from .config import number_of_ips
from .data import Data

data = Data()


def get_top_k_ips():
    largest = heapq.nlargest(number_of_ips, data.get_top_k_words())
    return list(map(lambda node: node[1], largest))