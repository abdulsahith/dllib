code = """
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

activations = ['sigmoid', 'relu', 'tanh', 'sigmoid']
epochs_list = [24, 25, 21, 23]
val_splits = [0.3, 0.2, 0.1, 0.2]

optimizers = [
    tf.keras.optimizers.Adagrad(0.001),
    tf.keras.optimizers.Adam(0.001),
    tf.keras.optimizers.Adadelta(0.001),
    tf.keras.optimizers.Adam(0.001)
]

(x_train, y_train), _ = mnist.load_data()
x_train = x_train / 255.0
y_train = to_categorical(y_train, 10)

for i in range(4):
    model = Sequential([
        Flatten(input_shape=(28, 28)),
        Dense(128, activation=activations[i]),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer=optimizers[i], loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(x_train, y_train, epochs=epochs_list[i], validation_split=val_splits[i], verbose=0)
    print(f"Scenario {i+1}: Activation={activations[i]}, Max Val Accuracy={max(history.history['val_accuracy']):.4f}")

"""

def run():
    print(code)
