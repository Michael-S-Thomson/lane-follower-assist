# Lane Follower Assist System (LFAS)

A computer vision and deep learning project exploring lane-scene understanding using a Convolutional Neural Network (CNN) for semantic image segmentation.

## Project Overview

The Lane Follower Assist System (LFAS) explores how computer vision can help a vehicle understand its driving environment. The project uses RGB camera images and corresponding segmentation masks to train a CNN to classify image pixels into semantic classes.

The long-term goal is to support lane awareness and safer vehicle positioning. The current model is a segmentation prototype and has not been validated as a real-time vehicle steering or safety system.

## Objectives

- Process RGB camera images and segmentation masks.
- Build a CNN-based semantic segmentation model.
- Train the model to predict pixel-level classes.
- Evaluate performance using validation accuracy and Intersection over Union (IoU).
- Explore class weighting to improve performance on less frequent classes.

## Dataset

The project uses the CARLA capture dataset available locally, with:

- 1,000 RGB images
- 1,000 corresponding segmentation masks
- Image dimensions of 272 × 400 pixels after preprocessing
- 13 semantic classes

The dataset is stored locally and excluded from the Git repository.

## Model Architecture

The CNN includes:

- Convolutional layers with ReLU activation
- Max-pooling layers for downsampling
- Upsampling layers for restoring spatial dimensions
- A final 1 × 1 convolution with softmax activation to predict 13 classes per pixel

The model contains approximately 167,309 trainable parameters.

## Training and Evaluation

The dataset was split into:

- Training set: 800 images
- Validation set: 200 images

An initial model was trained and evaluated. Class-weighted training was then used to give more importance to less frequent classes.

| Metric | Initial model | Class-weighted model |
|---|---:|---:|
| Validation accuracy | 77.20% | 80.43% |
| Mean IoU | 0.2935 | 0.3539 |

The class-weighted model improved mean IoU by approximately 0.0604. Validation accuracy and mean IoU measure different aspects of performance, so both are reported.

## Current Limitations

- Some rare classes still have low or zero IoU.
- Predictions do not perfectly match the reference segmentation masks.
- Semantic class IDs have not yet been fully mapped to their class names in the project documentation.
- Real-time performance has not been established.
- Vehicle steering control and road-safety validation have not been implemented and tested as part of this segmentation prototype.

## Future Improvements

- Map all 13 class IDs to their semantic labels.
- Improve segmentation of rare classes.
- Evaluate performance on unseen driving scenes.
- Add qualitative prediction visualizations and class-wise evaluation.
- Investigate real-time inference and integration with a lane-following controller.

## Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Jupyter Notebook
- Convolutional Neural Networks
- Semantic Image Segmentation
- Git and GitHub

## Project Structure

```text
LFAS/
├── src/
│   └── LFAS_code.ipynb
├── data/                 # Local dataset; excluded from Git
├── .gitignore
└── README.md
```

## How to Run

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the required Python packages.
4. Place the dataset in the expected local `data/` directory.
5. Open `src/LFAS_code.ipynb` in Jupyter Notebook and run the cells in order.

A `requirements.txt` file should be added with the package versions used by the working environment.

## Project Status

**Status:** Deep learning segmentation prototype — ongoing.

This project demonstrates dataset preprocessing, CNN model development, model training, class-imbalance handling, and evaluation using mean IoU.
