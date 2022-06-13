import matplotlib.pyplot as plt
import numpy as np

def plot_moons(X, y):
  """
  Plots moons with x1, x2 values stored in X and y values stored in y.
  """
  x1 = X[:, 0]
  x2 = X[:, 1]
  plt.scatter(x1, x2, c=y)

def plot_moons_predictions(X, y, model, x1_lim=(-2, 4), x2_lim=(-2, 2), plot_points=True):
  """
  Plots prediciton surface of a model within the bounds specified by the limits and
  additionally plots the original data points (can be turned off).
  """
  X1_linspace = np.linspace(x1_lim[0], x1_lim[1], 50)
  X2_linspace = np.linspace(x2_lim[0], x2_lim[1], 50)
  X1_mesh, X2_mesh = np.meshgrid(X1_linspace, X2_linspace)
  X1_flattened = X1_mesh.flatten()
  X2_flattened = X2_mesh.flatten()
  X_grid = np.array(list(zip(X1_flattened, X2_flattened)))

  preds = model(X_grid)
  preds_mesh = preds.numpy().reshape(50, 50)

  h = plt.contourf(X1_mesh, X2_mesh, preds_mesh)
  if plot_points:
    x1 = X[:, 0]
    x2 = X[:, 1]
    plt.scatter(x1, x2, c=y)
