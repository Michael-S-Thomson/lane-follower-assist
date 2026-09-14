import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random

from tqdm import notebook
from multiprocessing import Pool

from tensorflow import keras
from keras.models import Sequential, Model
from keras.layers import *
from keras.callbacks import ModelCheckpoint
import keras.backend as K
import tensorflow as tf
from keras.utils.vis_utils import plot_model
from keras.preprocessing.image import ImageDataGenerator


# Dataset location
src_dir = '../input/lyft-udacity-challenge/dataA/dataA'


# Get input image and mask filenames
input_imgs_names = os.listdir(
    os.path.join(src_dir, 'CameraRGB')
)

mask_names = os.listdir(
    os.path.join(src_dir, 'CameraSeg')
)


# Display a random input image and its mask
index = random.randint(0, len(input_imgs_names) - 1)

img = cv2.imread(
    os.path.join(
        src_dir,
        'CameraRGB',
        input_imgs_names[index]
    )
)

mask = cv2.imread(
    os.path.join(
        src_dir,
        'CameraSeg',
        mask_names[index]
    )
)

plt.figure()
plt.imshow(img)

plt.figure()
plt.imshow(mask[:, :, 2])


# Split segmentation mask into separate classes
def split_img(mask_img):

    new_mask_img = np.zeros(
        (mask_img.shape[0], mask_img.shape[1], 3)
    )

    for j in range(1, 4):
        for k in range(mask_img.shape[0]):
            for l in range(mask_img.shape[1]):

                if mask_img[k, l] == j:
                    new_mask_img[k, l, j - 1] = j

    return new_mask_img


# Output directory
dest_dir = '/kaggle/working/'

os.makedirs(
    os.path.join(dest_dir, 'Inputs'),
    exist_ok=True
)

os.makedirs(
    os.path.join(dest_dir, 'Outputs'),
    exist_ok=True
)


# Process a sample segmentation mask
N = 5

mask_img = cv2.imread(
    os.path.join(
        src_dir,
        'CameraSeg',
        mask_names[N]
    )
)

mask_img = cv2.resize(
    mask_img,
    (400, 272)
)

new_mask = np.zeros((272, 400))

new_mask[
    np.where(mask_img == 6)[0],
    np.where(mask_img == 6)[1]
] = 1

new_mask[
    np.where(mask_img == 7)[0],
    np.where(mask_img == 7)[1]
] = 2

new_mask[
    np.where(mask_img == 8)[0],
    np.where(mask_img == 8)[1]
] = 3

print(new_mask.shape)
print(mask_img.shape)

plt.figure()
plt.imshow(mask_img[:, :, 2])

plt.figure()
plt.imshow(
    new_mask.reshape(
        mask_img.shape[0],
        mask_img.shape[1]
    )
)


# Model compilation
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


# Model training
history = model.fit(
    input_images,
    mask_images,
    batch_size=32,
    epochs=50,
    validation_split=0.1
)


# Prediction
index = random.randint(0, 1000)

input_img = input_images[index]
output_img = mask_images[index]

img_ht = input_img.shape[0]
img_wd = input_img.shape[1]
img_ly = input_img.shape[2]

plt.figure()
plt.imshow(input_img)

plt.figure()
plt.imshow(
    output_img.reshape(
        output_img.shape[0],
        output_img.shape[1]
    )
)

print(input_img.shape)

pred = model.predict(
    input_img.reshape(
        (
            1,
            input_img.shape[0],
            input_img.shape[1],
            input_img.shape[2]
        )
    )
)


# Save trained model
model.save(
    '/kaggle/working/lane-road-seg-v1.h5'
)


# Load trained model
model4 = tf.keras.models.load_model(
    '/kaggle/working/lane-road-seg-v1.h5'
)

index = random.randint(0, 1000)

input_img = input_images[index]
output_img = mask_images[index]

img_ht = input_img.shape[0]
img_wd = input_img.shape[1]
img_ly = input_img.shape[2]

plt.figure()
plt.imshow(input_img)

plt.figure()
plt.imshow(
    output_img.reshape(
        output_img.shape[0],
        output_img.shape[1]
    )
)