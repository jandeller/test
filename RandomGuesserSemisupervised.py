import numpy as np

class RandomGuesserSemisupervised():

    def fit(self, X_train):
        pass
      
    def decision_function(self, X_test):
        "Assign a random number to each sample from the test set"
        n_samples = X_test.shape[0]
        return np.random.randn(n_samples)
