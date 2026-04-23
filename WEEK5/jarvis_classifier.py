import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))

    def predict(self, X):
        predictions = []
        for x in X:
            distances = [self.euclidean_distance(x, x_train)
                        for x_train in self.X_train]
            k_indices = np.argsort(distances)[:self.k]
            k_labels = [self.y_train[i] for i in k_indices]
            prediction = Counter(k_labels).most_common(1)[0][0]
            predictions.append(prediction)
        return np.array(predictions)

def jarvis_classify(data, labels, new_point, k=3):
    """
    Jarvis uses KNN to classify anything.
    data      = training features
    labels    = training categories  
    new_point = new thing to classify
    """
    knn = KNN(k=k)
    knn.fit(data, labels)
    result = knn.predict([new_point])
    print(f"Jarvis: I classify this as → {result[0]}")
    return result[0]

# Test Jarvis with simple example
if __name__ == "__main__":
    # Simple test - 2 categories
    training_data = np.array([
        [1, 2], [2, 3], [3, 1],   # Category A
        [8, 9], [9, 8], [8, 8]    # Category B
    ])
    training_labels = ["A", "A", "A", "B", "B", "B"]
    
    new_point = np.array([2, 2])
    
    print("Jarvis Classifier v1 - Online")
    print("="*40)
    jarvis_classify(training_data, training_labels, new_point)