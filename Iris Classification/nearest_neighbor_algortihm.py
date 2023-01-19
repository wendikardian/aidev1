
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# load dataset
X, y = load_iris(return_X_y=True)
# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the KNN classifier
class KNNClassifier:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = []
        for x in X:
            # Calculate the distance between x and each point in the training set
            distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
            # Get the indices of the k-nearest neighbors
            k_indices = np.argsort(distances)[:self.k]
            # Get the class labels of the k-nearest neighbors
            k_neighbors = [self.y_train[i] for i in k_indices]
            # Determine the class of x based on the majority class among the k-nearest neighbors
            y_pred.append(max(set(k_neighbors), key=k_neighbors.count))
        return y_pred

# Instantiate the classifier with k=3
knn = KNNClassifier(3)

# Train the classifier
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Calculate the accuracy of the predictions
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)
