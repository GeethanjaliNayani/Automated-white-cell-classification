# -*- coding: utf-8 -*-
"""WBC_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qx1us6wf8VtuwZOmHr4AJsFgnu4nVigb
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from sklearn.metrics import accuracy_score, classification_report

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from google.colab import drive
drive.mount('/content/drive')

ls drive

train_dir = '/content/drive/MyDrive/dataset2-master/dataset2-master/images/TRAIN'
test_dir = '/content/drive/MyDrive/dataset2-master/dataset2-master/images/TEST'

# Create generators

train_gen = tf.keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function = tf.keras.applications.mobilenet_v2.preprocess_input ,
    validation_split= 0.2
)

test_gen = tf.keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function = tf.keras.applications.mobilenet_v2.preprocess_input ,
    validation_split= 0.2
)

# Flow image data

train_images = train_gen.flow_from_directory(
    directory = train_dir , target_size = (224,224) , color_mode = 'rgb' ,
    class_mode = 'categorical' , batch_size = 32 , shuffle= True , seed = 42,
    subset = 'training'
)

val_images = train_gen.flow_from_directory(
    directory = train_dir , target_size = (224,224) , color_mode = 'rgb' ,
    class_mode = 'categorical' , batch_size = 32 , shuffle= True , seed = 42,
    subset = 'validation'
)


test_images = test_gen.flow_from_directory(
    directory = test_dir , target_size = (224,224) , color_mode = 'rgb' ,
    class_mode = 'categorical' , batch_size = 32 , shuffle= False , seed = 42
)

# Load the MobileNetV2 model
pretrained_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet',
    pooling='avg'
)

# Fine-tune the last few layers of the pretrained model
for layer in pretrained_model.layers[:-10]:
    layer.trainable = False

# Build a custom head on top of the pretrained model
model = models.Sequential()
model.add(pretrained_model)
model.add(layers.Dense(256, activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.4))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.4))
model.add(layers.Dense(4, activation='softmax'))

# Compile the model
model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)



# Data Augmentation
train_datagen = ImageDataGenerator(
    preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Display the model summary
model.summary()

# Training Data Generator with Augmentation
train_images_augmented = train_datagen.flow_from_directory(
    directory=train_dir,
    target_size=(224, 224),
    color_mode='rgb',
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    seed=42,
    subset='training'
)

# Training with Augmented Data
history = model.fit(
    train_images_augmented,
    validation_data=val_images,
    epochs=100,
    callbacks=[
        EarlyStopping(
            monitor='val_loss',
            patience=15,
            restore_best_weights=True
        )
    ]
)

import pandas as pd
import matplotlib.pyplot as plt

# Assuming `history` is the result from the training
train_accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']

# Create a DataFrame
history_df = pd.DataFrame({
    'Epoch': range(1, len(train_accuracy) + 1),
    'Train_Accuracy': train_accuracy,
    'Validation_Accuracy': val_accuracy
})

# Display the DataFrame
print(history_df)

# Save the DataFrame to a CSV file
history_df.to_csv('training_history.csv', index=False)

# Plot training and validation accuracy over epochs
plt.plot(history_df['Epoch'], history_df['Train_Accuracy'], label='Train Accuracy')
plt.plot(history_df['Epoch'], history_df['Validation_Accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy Over Epochs')
plt.legend()
plt.show()

fig = px.line(
    history.history,
    y=['loss', 'val_loss'],
    labels={'index': 'Epoch', 'value': 'Loss'},
    title='Training and Validation Loss Over Time'
)

fig.show()

CLASS_NAMES = list(train_images.class_indices.keys())
CLASS_NAMES

predictions = np.argmax(model.predict(test_images) , axis=1)

acc = accuracy_score(test_images.labels , predictions)

cm = tf.math.confusion_matrix(test_images.labels , predictions)
clr = classification_report(test_images.labels , predictions , target_names = CLASS_NAMES)

print("Test Accuracy: {:.3f}%".format(acc * 100))

plt.figure(figsize=(8, 8))
sns.heatmap(cm, annot=True, fmt='g', vmin=0, cmap='Blues', cbar=False)
plt.xticks(ticks= np.arange(4) + 0.5, labels=CLASS_NAMES)
plt.yticks(ticks= np.arange(4) + 0.5, labels=CLASS_NAMES)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

print("Classification Report:\n----------------------\n", clr)

# Make predictions on the test images
predictions = model.predict(test_images)

# Get the predicted class indices
predicted_class_indices = np.argmax(predictions, axis=1)

# Visualize results for a few test images
import random
import os


num_images_to_display = 20

# Get a random order of indices
random_indices = random.sample(range(len(test_images.filenames)), num_images_to_display)

for i in random_indices:
    # Get the image and true label
    img_path = os.path.join(test_dir, test_images.filenames[i])
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    true_label = CLASS_NAMES[test_images.labels[i]]

    # Get the predicted label
    predicted_label = CLASS_NAMES[predicted_class_indices[i]]

    # Display the image and labels
    plt.imshow(img_array[0] / 255.0)
    plt.title(f'True: {true_label}, Predicted: {predicted_label}')
    plt.show()

# Assuming 'model' is your trained model
model.save('blood_cell_classifier.h5')

# Load the saved model
loaded_model = tf.keras.models.load_model('blood_cell_classifier.h5')

# Save the model architecture to a JSON file
model_json = model.to_json()
with open('blood_cell_classifier.json', 'w') as json_file:
    json_file.write(model_json)

# Save the learned weights to an HDF5 file
model.save_weights('blood_cell_classifier_weights.h5')

# Load the model architecture from the JSON file
with open('blood_cell_classifier.json', 'r') as json_file:
    loaded_model_json = json_file.read()

loaded_model = tf.keras.models.model_from_json(loaded_model_json)

# Load the learned weights
loaded_model.load_weights('blood_cell_classifier_weights.h5')

from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('blood_cell_classifier.h5')

# Define the class names
CLASS_NAMES = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']

def preprocess_image(image_path):
    img = Image.open(image_path).resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['image']

    # Save the image temporarily
    temp_image_path = 'temp_image.jpg'
    file.save(temp_image_path)

    # Preprocess the image
    img_array = preprocess_image(temp_image_path)

    # Make predictions
    predictions = model.predict(img_array)

    # Get the predicted class
    predicted_class = CLASS_NAMES[np.argmax(predictions)]

    # Remove the temporary image file
    os.remove(temp_image_path)

    return jsonify({'prediction': predicted_class})

if __name__ == '__main__':
    app.run(debug=True, port=8080)

python app.py

curl -X POST -F "image=@path/to/your/image.jpg" http://127.0.0.1:5000/predict