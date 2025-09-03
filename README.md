This project implements a hand gesture recognition system using OpenCV, MediaPipe, and Random Forest Classifier. The system captures images of hand gestures, extracts key landmark features, trains a classifier, and performs real-time gesture recognition using a webcam.

🚀 Project Workflow

Data Collection (collect_imgs.py)

Uses a webcam to capture images for multiple gesture classes.

Stores images in separate directories for each class.

Press 'Q' to start collecting and to stop capturing.

Dataset Creation (create_dataset.py)

Extracts hand landmarks (x, y coordinates) using MediaPipe Hands.

Normalizes landmarks relative to the minimum x and y positions.

Stores extracted features and labels in data.pickle.

Model Training (train_classifier.py)

Loads landmark dataset from data.pickle.

Trains a Random Forest Classifier to distinguish between gestures.

Splits dataset into training and testing sets.

Evaluates accuracy and saves the trained model in model.p.

Inference / Real-Time Recognition (inference_classifier.py)

Loads trained model (model.p).

Uses webcam feed for real-time gesture detection.

MediaPipe extracts landmarks from each frame.

The trained classifier predicts the gesture (e.g., "A", "B", "L").

Bounding boxes and predicted labels are displayed on the video feed.

🛠️ Technologies Used

Python

OpenCV → For image capture and visualization

MediaPipe Hands → For hand landmark detection

Scikit-learn → For model training (Random Forest Classifier)

Pickle → For saving dataset and trained model
