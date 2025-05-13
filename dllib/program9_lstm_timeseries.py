code = """
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

series = np.sin(np.linspace(0, 100, 1000))
X, y = [], []
for i in range(50, len(series)):
    X.append(series[i-50:i])
    y.append(series[i])
X = np.array(X).reshape(-1, 50, 1)
y = np.array(y)

model = Sequential([
    LSTM(50, activation='relu', input_shape=(50, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=20)
"""

def run():
    print(code)
