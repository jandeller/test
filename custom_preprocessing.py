import numpy as np

def scale_values(values: np.ndarray, scaling_factor: float, message: str):
    print(message)
    return values * scaling_factor
