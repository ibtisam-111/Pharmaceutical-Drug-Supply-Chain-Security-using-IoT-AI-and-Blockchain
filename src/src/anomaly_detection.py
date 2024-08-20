import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import OneClassSVM

def detect_anomalies(data):
    model = OneClassSVM(kernel='rbf', gamma='auto').fit(data)
    predictions = model.predict(data)
    return predictions

# Example usage
data = np.random.rand(100, 5)
anomalies = detect_anomalies(data)
print('Anomalies:', anomalies)
