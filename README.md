# 🚗 Lane Follower Assist System (LFAS)

A Lane Follower Assist System designed to improve vehicle safety by detecting and tracking lane information and assisting with proper vehicle lane positioning.

## 📌 Project Overview

The **Lane Follower Assist System (LFAS)** is a computer vision and machine learning project focused on assisting vehicles with lane-following tasks.

The system processes road-camera images, performs image preprocessing, and uses a machine learning model to classify the input image into lane-related classes.

The project uses road images captured from the **CARLA simulator** and demonstrates the application of computer vision and machine learning concepts in intelligent transportation and autonomous driving.

## 🎯 Objectives

* Detect and recognize lane-related information from road images.
* Process camera data for machine learning.
* Prepare and preprocess road images.
* Train a machine learning model for image classification.
* Assist with maintaining proper lane positioning.
* Explore computer vision applications in autonomous driving.
* Provide a foundation for future lane-following improvements.
* Evaluate model predictions and classification performance.

## 🏗️ System Architecture

The LFAS concept combines the following components:

* Camera/sensor input
* Image preprocessing
* Lane-related information extraction
* Data processing
* Machine learning
* Classification
* Prediction
* Lane-following assistance

The overall system can be represented as:

```text
Camera / Sensor Input
        ↓
Road Image
        ↓
Image Preprocessing
        ↓
Data Preparation
        ↓
Machine Learning Model
        ↓
Class Prediction
        ↓
Lane Information
        ↓
Lane-Following Assistance
```

## 🔄 System Workflow

```text
Road Images
     ↓
Data Collection
     ↓
Data Preprocessing
     ↓
Image Preparation
     ↓
Feature / Image Representation
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Image Prediction
     ↓
Class Prediction
     ↓
Lane-Following Assistance
```

## 🛠️ Technologies & Tools

### Programming & Development

* Python
* Jupyter Notebook
* Google Colab

### Data Processing

* NumPy
* Pandas
* Matplotlib
* Seaborn

### Machine Learning & Deep Learning

* Scikit-learn
* TensorFlow
* Keras
* Neural Network Classification

### Computer Vision

* OpenCV

### Dataset / Simulation

* CARLA Simulator

## 🤖 Machine Learning

The current implementation uses a **TensorFlow/Keras neural-network model** for image classification.

The model receives a preprocessed road image and produces predictions across multiple classes.

### Machine Learning Workflow

1. Data loading
2. Data preprocessing
3. Image preparation
4. Dataset preparation
5. Model building
6. Model training
7. Model evaluation
8. Image prediction
9. Class prediction

### Model Prediction

For an input image, the trained model produces class probabilities and identifies the predicted class.

Example:

```text
Prediction shape: (1, 10)
Predicted class: 8
```

The model therefore produces predictions across **10 classes**.

## 📚Project Report

The  project documentation describes a broader LFAS architecture involving sensor technologies, lane detection, control algorithms, steering adjustment, and machine-learning approaches.

The current implementation focuses primarily on **camera-image processing and machine-learning classification**.

This repository therefore distinguishes between the concepts described in the original project report and the components implemented in the current code.

## 🗄️ Data Processing

The project uses road images generated from the CARLA simulator.

The dataset contains camera-based road images used for training and testing the machine learning model.

The data-processing workflow includes:

* Loading images
* Image preprocessing
* Image resizing
* Data preparation
* Model input preparation
* Model prediction

Large dataset files are not included in this repository.

## 📂 Project Structure

```text
lane-follower-assist/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── LFAS_code.py
│
├── data/
│   └── carla-capture-20180513A/
│       ├── CameraRGB/
│       └── CameraSeg/
│
└── docs/
    └── project-report.pdf
```

> **Note:** The `data/` directory is excluded from GitHub because the dataset contains a large number of image files.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Michael-S-Thomson/lane-follower-assist.git
```

### 2. Open the project directory

```bash
cd lane-follower-assist
```

### 3. Create a virtual environment

```bash
python -m venv lfas-env
```

### 4. Activate the environment on Windows

```bash
lfas-env\Scripts\activate
```

### 5. Install the required libraries

```bash
pip install -r requirements.txt
```

## 📦 Required Libraries

The main Python dependencies are:

```text
numpy
pandas
matplotlib
opencv-python
tensorflow
scikit-learn
jupyter
```

## ▶️ How to Run

After installing the required dependencies:

1. Activate the virtual environment.
2. Place the required CARLA dataset in the appropriate local `data/` directory.
3. Open the Jupyter Notebook or Python source code.
4. Run the preprocessing and model code.
5. Provide an input road image.
6. Run the trained model for prediction.
7. View the predicted class and class probabilities.

Example:

```text
Input Image
     ↓
Preprocessing
     ↓
TensorFlow/Keras Model
     ↓
Prediction
     ↓
Predicted Class
```

## 📊 Results

The current implementation successfully generates predictions for input road images.

Example model output:

```text
Prediction Shape : (1, 10)
Predicted Class  : 8
```

The model also produces a probability distribution across the 10 available classes.

Example:

```text
Class 0 : 10.49%
Class 1 : 10.34%
Class 2 : 10.36%
Class 3 :  9.57%
Class 4 : 11.14%
Class 5 :  9.12%
Class 6 :  8.76%
Class 7 : 10.18%
Class 8 : 11.37%
Class 9 :  8.66%
```

These results demonstrate the prediction pipeline, while further training and evaluation are required to improve classification confidence and real-world performance.

## ✅ Advantages

* Demonstrates computer vision for intelligent transportation.
* Applies machine learning to road-image classification.
* Provides a foundation for lane-following assistance.
* Can be extended with real-time camera input.
* Can be integrated with additional vehicle sensors.
* Provides opportunities for further autonomous-driving research.
* Can be improved using larger datasets and advanced models.

## 🚀 Future Enhancements

Future development can include:

* Improve lane-detection accuracy.
* Increase the size and diversity of the training dataset.
* Experiment with advanced CNN architectures.
* Improve image preprocessing.
* Add real-time video input.
* Implement real-time lane detection.
* Integrate steering-control algorithms.
* Test the system in the CARLA simulator in real time.
* Improve handling of curves and intersections.
* Support complex urban road environments.
* Integrate additional sensors such as LiDAR and radar.
* Explore V2X (Vehicle-to-Everything) communication.
* Improve system safety and validation.

## 📄 Project Documentation

The complete project report is available in this repository:

**Lane Follower Assist Final Report**

The report provides additional information about the project concept, system architecture, technologies, testing, and future enhancements.

## 👨‍💻 Author

### Michael Singarayar Thomson

**Aspiring Data Scientist | AI & Machine Learning Enthusiast**

### Skills

* Python
* SQL
* Machine Learning
* Deep Learning
* Pandas
* NumPy
* Data Analysis
* Power BI
* OpenCV
* TensorFlow
* Git & GitHub

## 🔗 Repository

**GitHub:**
https://github.com/Michael-S-Thomson/lane-follower-assist

---
