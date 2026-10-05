# Assignment: Cat vs Dog Image Classifier
# Part-2: Model Training, Evaluation and Prediction

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras import layers, models
from tensorflow.keras.utils import load_img, img_to_array


# --------------------------------------------------
# 1. Set parameters
# --------------------------------------------------

IMG_SIZE = (150, 150)
BATCH_SIZE = 32
EPOCHS = 10


# --------------------------------------------------
# 2. Load training and validation data
# --------------------------------------------------

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


# --------------------------------------------------
# 3. Normalize images
# --------------------------------------------------

normalization_layer = layers.Rescaling(1.0 / 255)

train_data = train_data.map(
    lambda x, y: (normalization_layer(x), y)
)

validation_data = validation_data.map(
    lambda x, y: (normalization_layer(x), y)
)


# --------------------------------------------------
# 4. Create CNN model
# --------------------------------------------------

model = models.Sequential([
    layers.Input(shape=(150, 150, 3)),

    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),

    layers.Dense(128, activation="relu"),

    layers.Dense(1, activation="sigmoid")
])


# --------------------------------------------------
# 5. Compile model
# --------------------------------------------------

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# --------------------------------------------------
# 6. Display model structure
# --------------------------------------------------

model.summary()


# --------------------------------------------------
# 7. Train the model
# --------------------------------------------------

history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=EPOCHS
)


# --------------------------------------------------
# 8. Evaluate the model
# --------------------------------------------------

loss, accuracy = model.evaluate(validation_data)

print("\nModel Evaluation")
print("-----------------")
print("Validation Loss:", loss)
print("Validation Accuracy:", accuracy)


# --------------------------------------------------
# 9. Plot training and validation accuracy
# --------------------------------------------------

plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

plt.title("Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()


# --------------------------------------------------
# 10. Plot training and validation loss
# --------------------------------------------------

plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")

plt.title("Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()


# --------------------------------------------------
# 11. Function to predict Cat or Dog
# --------------------------------------------------

def predict_image(image_path):

    # Load image
    image = load_img(
        image_path,
        target_size=IMG_SIZE
    )

    # Convert image to array
    image_array = img_to_array(image)

    # Normalize pixel values
    image_array = image_array / 255.0

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # Make prediction
    prediction = model.predict(image_array, verbose=0)[0][0]

    # Display image
    plt.imshow(image)
    plt.axis("off")

    # Classify image
    if prediction >= 0.5:
        result = "Dog"
        confidence = prediction * 100
    else:
        result = "Cat"
        confidence = (1 - prediction) * 100

    print("Prediction:", result)
    print("Confidence: {:.2f}%".format(confidence))

    plt.title(
        "Prediction: {} ({:.2f}%)".format(result, confidence)
    )
    plt.show()


# --------------------------------------------------
# 12. Test the model
# --------------------------------------------------

predict_image("test.jpg")