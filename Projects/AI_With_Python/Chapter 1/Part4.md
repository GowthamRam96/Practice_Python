# Naive bayes Classifier
Naïve Bayes is a technique used to build classifiers using Bayes theorem. Bayes theorem
describes the probability of an event occurring based on different conditions that are related to
this event. We build a Naïve Bayes classifier by assigning class labels to problem instances.
These problem instances are represented as vectors of feature values. The assumption here is
that the value of any given feature is independent of the value of any other feature. This is
called the independence assumption, which is the naïve part of a Naïve Bayes classifier.


```py
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import naive_bayes

from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection

def visualize_classifier(classifier, X, y):
    # Define the minimum and maximum values for X and Y
    # that will be used in the mesh grid
    min_x, max_x = X[:, 0].min() - 1.0, X[:, 0].max() + 1.0
    min_y, max_y = X[:, 1].min() - 1.0, X[:, 1].max() + 1.0
    # Define the step size to use in plotting the mesh grid
    mesh_step_size = 0.01
    # Define the mesh grid of X and Y values
    x_vals, y_vals = np.meshgrid(np.arange(min_x, max_x,
                                           mesh_step_size), np.arange(min_y, max_y, mesh_step_size))
    # Run the classifier on the mesh grid
    output = classifier.predict(np.c_[x_vals.ravel(), y_vals.ravel()])
    # Reshape the output array
    output = output.reshape(x_vals.shape)
    # Create a plot
    plt.figure()
    # Choose a color scheme for the plot
    plt.pcolormesh(x_vals, y_vals, output, cmap=plt.cm.gray)
    # Overlay the training points on the plot
    plt.scatter(X[:, 0], X[:, 1], c=y, s=75, edgecolors='black',
                linewidth=1, cmap=plt.cm.Paired)

    # Specify the boundaries of the plot
    plt.xlim(x_vals.min(), x_vals.max())
    plt.ylim(y_vals.min(), y_vals.max())
    # Specify the ticks on the X and Y axes
    plt.xticks((np.arange(int(X[:, 0].min() - 1), int(X[:, 0].max() +
                                                      1), 1.0)))
    plt.yticks((np.arange(int(X[:, 1].min() - 1), int(X[:, 1].max() +
                                                      1), 1.0)))
    plt.show()

# Input file containing data
input_file = 'data_multivar_nb.txt'

# Load data from input file
data = np.loadtxt(input_file, delimiter=',')
X, y = data[:, :-1], data[:, -1]

# Create Naïve Bayes classifier
classifier = GaussianNB()

# Train the classifier
classifier.fit(X, y)

# Predict the values for training data
y_pred = classifier.predict(X)

# Compute accuracy
accuracy = 100.0 * (y == y_pred).sum() / X.shape[0]
print("Accuracy of Naïve Bayes classifier =", round(accuracy, 2), "%")
# Visualize the performance of the classifier
visualize_classifier(classifier, X, y)

# Split data into training and test data
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=3)
classifier_new = GaussianNB()
classifier_new.fit(X_train, y_train)
y_test_pred = classifier_new.predict(X_test)


# compute accuracy of the classifier
accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
print("Accuracy of the new classifier =", round(accuracy, 2), "%")
# Visualize the performance of the classifier
visualize_classifier(classifier_new, X_test, y_test)


num_folds = 3
accuracy_values = model_selection.cross_val_score(classifier,
X, y, scoring='accuracy', cv=num_folds)
print("Accuracy: " + str(round(100*accuracy_values.mean(), 2)) + "%")
precision_values = model_selection.cross_val_score(classifier,
X, y, scoring='precision_weighted', cv=num_folds)
print("Precision: " + str(round(100*precision_values.mean(), 2)) +
"%")
recall_values = model_selection.cross_val_score(classifier,
X, y, scoring='recall_weighted', cv=num_folds)
print("Recall: " + str(round(100*recall_values.mean(), 2)) + "%")
f1_values = model_selection.cross_val_score(classifier,
X, y, scoring='f1_weighted', cv=num_folds)
print("F1: " + str(round(100*f1_values.mean(), 2)) + "%")
```

# Results
Accuracy of Naïve Bayes classifier = 99.75 %

Accuracy of the new classifier = 100.0 %

Accuracy: 99.75%

Precision: 99.76%

Recall: 99.75%

F1: 99.75%

![image](https://user-images.githubusercontent.com/84629235/147831193-efdc3540-2483-4baa-92f7-078c8b69584f.png)

![image](https://user-images.githubusercontent.com/84629235/147831205-d06a6802-c041-4577-9579-572fe7006043.png)
