import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Preprocessing Input data
# data = pd.read_csv('20K_Datapoints.csv')
data = pd.read_csv('20K_Datapoints.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)
plt.show()

# Building the model
a = 0
b = 0
c = 0

L = 0.0001  # The learning Rate
epochs = 10000  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# Performing Gradient Descent 
for i in range(epochs): 
    Y_pred = a*X*X + b*X + c  # The current predicted value of Y
    D_a = (-2/n) * sum(X*X * (Y - Y_pred))  # Derivative wrt a
    D_b = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt b
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    a = a - L * D_a  # Update a
    b = b - L * D_b  # Update b
    c = c - L * D_c  # Update c

print (a, b, c)

# Making predictions
Y_pred = a*X*X + b*X + c

plt.scatter(X, Y)
plt.scatter(X, Y_pred , color='red') # predicted
plt.show()