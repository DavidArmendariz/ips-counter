class DataSingleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(DataSingleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]


class Data(metaclass=DataSingleton):
    def __init__(self):
        self.frequencies = {}
        self.top_k_words = []

    def set_frequencies(self, frequencies):
        self.frequencies = frequencies

    def get_frequencies(self):
        return self.frequencies

    def set_top_k_words(self, top_k_words):
        self.top_k_words = top_k_words

    def get_top_k_words(self):
        return self.top_k_words
