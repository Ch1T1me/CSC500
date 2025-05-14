# Author: Chioma Chance
# Assignment: Critical Thinking Assignment – Hand-Made ANN
# Description: This script trains a simple artificial neural network using NumPy to learn basic addition.
# It demonstrates feedforward, backpropagation, weight updates, and user input prediction.

import numpy as np

# Step 1: Training Data (learn x1 + x2)
X = np.array([
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 1],
    [4, 2],
    [5, 5],
    [6, 2],
    [7, 1],
    [8, 0],
    [9, 1],
    [3, 7],
    [6, 4],
    [4, 6],
    [5, 3]
], dtype=float)

y = np.array([
    [0],
    [2],
    [4],
    [4],
    [6],
    [10],
    [8],
    [8],
    [8],
    [10],
    [10],
    [10],
    [10],
    [8]
], dtype=float)

# Step 2: Normalize Data
X_max = np.max(X)
y_max = np.max(y)
X = X / X_max
y = y / y_max

# Step 3: Setup ANN Structure
np.random.seed(1)
input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1
epochs = 1000

W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))

# Activation function + derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Step 4: Training loop
for epoch in range(epochs):
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)

    loss = np.mean((y - a2) ** 2)

    # Backpropagation
    d_output = (y - a2) * sigmoid_derivative(a2)
    d_hidden = np.dot(d_output, W2.T) * sigmoid_derivative(a1)

    # Update weights
    W2 += np.dot(a1.T, d_output) * learning_rate
    b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    W1 += np.dot(X.T, d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Step 5: Prediction Function
def predict(x1, x2):
    x = np.array([[x1, x2]]) / X_max
    h = sigmoid(np.dot(x, W1) + b1)
    o = sigmoid(np.dot(h, W2) + b2)
    return o * y_max

# Step 6: Test Predictions
print("\nTest Predictions:")
print(f"[2 + 2] → Predicted: {predict(2, 2)[0][0]:.2f} (Expected: 4)")
print(f"[5 + 5] → Predicted: {predict(5, 5)[0][0]:.2f} (Expected: 10)")
print(f"[1 + 3] → Predicted: {predict(1, 3)[0][0]:.2f} (Expected: 4)")

# Step 7: Interactive Prediction
print("\nTry it yourself:")
x1 = float(input("Enter first number: "))
x2 = float(input("Enter second number: "))
pred = predict(x1, x2)[0][0]
print(f"Predicted sum: {pred:.2f}")
