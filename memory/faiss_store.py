import faiss
import os
import numpy as np
from config import FAISS_PATH

class FAISSStore:
    def __init__(self, dim=3072):
        self.dim = dim
        if os.path.exists(FAISS_PATH):
            self.index = faiss.read_index(FAISS_PATH)
        else:
            self.index = faiss.IndexFlatL2(dim)

    def is_empty(self):
        return self.index.ntotal == 0

    def add(self, vector):
        self.index.add(np.array([vector]).astype("float32"))
        faiss.write_index(self.index, FAISS_PATH)

    def search(self, vector, k=3):
        return self.index.search(
            np.array([vector]).astype("float32"), k
        )
