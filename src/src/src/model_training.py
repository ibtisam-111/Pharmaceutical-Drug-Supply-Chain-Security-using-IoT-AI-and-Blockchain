import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Assuming data has been preprocessed and split into features (X) and labels (y)
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Example usage
X = np.random.rand(1000, 20)
y = np.random.randint(0, 2, 1000)
accuracy = train_model(X, y)
print('Model Accuracy:', accuracy)
