import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        bow = set()
        corpus = positive + negative
        for document in corpus:
            for word in document.split():
                bow.add(word)
        
        bow = sorted(list(bow))
        word2int = {}
        for i, key in enumerate(bow):
            word2int[key] = i + 1

        def tokenize(document):
            tokens = []
            for token in document.split():
                tokens.append(word2int[token])
            return tokens
        
        tokenized = []
        for document in corpus:
           tokenized.append(torch.tensor(tokenize(document))) 

        return nn.utils.rnn.pad_sequence(tokenized, batch_first = True)