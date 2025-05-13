code = """
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Generate synthetic time series
sales_data = np.sin(np.linspace(0, 100, 1000)).reshape(-1, 1)
X, y = [], []
for i in range(10, len(sales_data)):
    X.append(sales_data[i-10:i])
    y.append(sales_data[i])
X, y = np.array(X), np.array(y)

# Build RNN model
model = Sequential([
    SimpleRNN(50, activation='relu', input_shape=(10, 1)),
    Dense(1)
])

# Compile and train
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=20)
"""

def run():
    print(code)
