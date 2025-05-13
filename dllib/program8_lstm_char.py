code = """
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical

text = "hello deep learning"
chars = sorted(set(text))
char_to_idx = {c: i for i, c in enumerate(chars)}
idx_to_char = {i: c for c, i in char_to_idx.items()}

seq_length = 3
X, y = [], []
for i in range(len(text) - seq_length):
    X.append([char_to_idx[c] for c in text[i:i+seq_length]])
    y.append(char_to_idx[text[i+seq_length]])

X = to_categorical(X, num_classes=len(chars))
y = to_categorical(y, num_classes=len(chars))

model = Sequential([
    LSTM(50, input_shape=(seq_length, len(chars))),
    Dense(len(chars), activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(X, y, epochs=500, verbose=0)
"""

def run():
    print(code)
