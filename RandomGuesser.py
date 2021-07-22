import numpy as np

class RandomGuesser():

    def fit(self, X):
        "Assign a random number to each sample"
        n_samples = X.shape[0]
        self.decision_scores_ = np.random.randn(n_samples)
