from .data import Data

data = Data()


def clear_data():
    data.set_frequencies({})
    data.set_top_k_words([])
