import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self, vocabulary_size: int):
        super().__init__()
        torch.manual_seed(0)
        
        self.embeddings = nn.Embedding(vocabulary_size, 16)
        self.classifier = nn.Linear(16, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x: TensorType[int]) -> TensorType[float]:
        # Hint: The embedding layer outputs a B, T, embed_dim tensor
        # but you should average it into a B, embed_dim tensor before using the Linear layer
        # Return a B, 1 tensor and round to 4 decimal places
        emgeddings = self.embeddings(x)
        x = self.classifier(torch.mean(emgeddings, axis=1))

        return torch.round(self.sigmoid(x), decimals=4)
