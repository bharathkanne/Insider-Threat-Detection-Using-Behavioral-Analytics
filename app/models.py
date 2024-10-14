from sklearn.ensemble import IsolationForest
import numpy as np

# Example: Train an Isolation Forest model on user activity data
def train_model(data):
    # Assuming 'data' is a DataFrame with feature columns
    model = IsolationForest()
    model.fit(data[['feature1', 'feature2']])  # Replace with actual feature columns
    return model
