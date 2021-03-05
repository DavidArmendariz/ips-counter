import heapq
from .data import Data
from .config import number_of_ips

data = Data()


def store_ip(ip: str):
    frequencies = data.get_frequencies()
    if ip in frequencies:
        frequencies[ip]["count"] += 1
    else:
        frequencies[ip] = {"count": 1, "index_in_heap": -1}
    min_heap = data.get_top_k_words()
    index_in_heap = frequencies[ip]["index_in_heap"]
    count = frequencies[ip]["count"]
    if index_in_heap == -1:
        if len(min_heap) <= number_of_ips:
            min_heap.append((count, ip))
        else:
            if count > min_heap[0]:
                _, oldMinIp = heapq.heapreplace(min_heap, count)
                frequencies[oldMinIp]["index_in_heap"] = -1
    else:
        min_heap[index_in_heap] = min_heap[-1]
        min_heap[-1] = (count, ip)
        heapq.heapify(min_heap)
    for index, value in enumerate(min_heap):
        _, ip = value
        frequencies[ip]["index_in_heap"] = index
    data.set_frequencies(frequencies)