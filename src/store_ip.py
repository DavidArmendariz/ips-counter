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
    # If the ip is not in the min heap, then the index_in_heap will be -1
    if index_in_heap == -1:
        # If we have not filled the min heap yet, keep adding elements to it!
        if len(min_heap) <= number_of_ips:
            min_heap.append((count, ip))
        # If the min heap is full, we have to check if the count of the current ip is greater than
        # the min element in the min heap. If not, we do nothing.
        # Else, we pop the previous min element and push the new ip. Also, we need to make sure
        # that the index_in_heap of the previous min element is set to -1 again
        else:
            if count > min_heap[0]:
                _, oldMinIp = heapq.heapreplace(min_heap, count)
                frequencies[oldMinIp]["index_in_heap"] = -1
    # If the ip is in the min heap...
    else:
        # We should replace the node in the min heap with the latest count
        min_heap[index_in_heap] = (count, ip)
        # and heapify again as the current node could now be greater than the children
        heapq.heapify(min_heap)
    # In case the indexes of the nodes messed up after the heapifying process, we should re-set
    # the indexes of the ips in the min heap
    for index, value in enumerate(min_heap):
        _, ip = value
        frequencies[ip]["index_in_heap"] = index
    data.set_frequencies(frequencies)