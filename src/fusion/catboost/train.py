import torch
import numpy as np
from catboost import CatBoostClassifier
from src.naive_dnn.utils import compute_eer

# Generate synthetic data
def train(X_train, y_train, X_test, y_test) :
    print("START TRAINING")

    # Initialize the CatBoost classifier
    model = CatBoostClassifier(iterations=50, depth=10, learning_rate=0.05, loss_function='Logloss', verbose=True)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    eer = compute_eer(y_test, y_pred)
    print(f'Accuracy: {eer}')