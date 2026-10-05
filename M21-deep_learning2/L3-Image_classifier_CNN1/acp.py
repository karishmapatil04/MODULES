# Assignment: Classify whether Cat or Dog
# Part-1: Data Preprocessing and Baseline Model

import tensorflow as tf
from tensorflow.keras import layers, models

# -----------------------------
# 1. Set image parameters
# -----------------------------

IMG_SIZE = (150, 150)
BATCH_SIZE = 32

# -----------------------------
# 2. Load and preprocess data
# -----------------------------

train_data = tf.keras.utils.image_dataset_from_directory(
    "dataset/train",
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="binary"
)

validation_data = tf.keras.utils.image_dataset_from_directory(
    "dataset/validation",
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="binary"
)

# -----------------------------
# 3. Normalize image pixels
# -----------------------------

normalization_layer = layers.Rescaling(1./255)

train_data = train_data.map(
    lambda x, y: (normalization_layer(x), y)
)

validation_data = validation_data.map(
    lambda x, y: (normalization_layer(x), y)
)

# -----------------------------
# 4. Create baseline CNN model
# -----------------------------

model = models.Sequential([
    
    # Input layer
    layers.Input(shape=(150, 150, 3)),

    # Convolution + Pooling
    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D(),

    # Second Convolution + Pooling
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D(),

    # Flatten
    layers.Flatten(),

    # Fully connected layer
    layers.Dense(128, activation="relu"),

    # Output layer
    layers.Dense(1, activation="sigmoid")
])

# -----------------------------
# 5. Compile the model
# -----------------------------

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# -----------------------------
# 6. Display model summary
# -----------------------------

model.summary()

# -----------------------------
# 7. Train the baseline model
# -----------------------------

history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=10
)

# -----------------------------
# 8. Evaluate the model
# -----------------------------

loss, accuracy = model.evaluate(validation_data)

print("\nValidation Accuracy:", accuracy)
print("Validation Loss:", loss)