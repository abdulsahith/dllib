code = """
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate sample data
X, y = make_regression(n_samples=1000, n_features=5, noise=0.1)
X = (X - np.min(X)) / (np.max(X) - np.min(X))

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build model
model = Sequential([
    Dense(64, input_dim=5, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)
])

# Compile and train
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))
"""

def run():
    print(code)
