import numpy as np
from numpy.typing import NDArray


# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

class Solution:
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)
        ans: list[float] = []
        
        for item in X:
            ans.append(round(np.matmul(item, weights), 5))
        return ans


    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        model_prediction, ground_truth = np.array(model_prediction), np.array(ground_truth)
        assert model_prediction.shape == ground_truth.shape, 'arrays are not equal length'
        
        mse = np.mean([(pred-gt)**2 for pred, gt in zip(model_prediction, ground_truth)])
        return np.round(mse, 5)