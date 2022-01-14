# Decision Tree
A **Decision Tree** is a structure that allows us to split the dataset into branches and then make
simple decisions at each level. This will allow us to arrive at the final decision by walking down
the tree. Decision Trees are produced by training algorithms, which identify how we can split
the data in the best possible way.

# Code
```py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier

from utilities import visualize_classifier

# Load input data
input_file = 'data_decision_trees.txt'
data = np.loadtxt(input_file, delimiter=',')
X, y = data[:, :-1], data[:, -1]

# Separate input data into two classes based on labels
class_0 = np.array(X[y==0])
class_1 = np.array(X[y==1])

# Visualize input data
plt.figure()
plt.scatter(class_0[:, 0], class_0[:, 1], s=75, facecolors='black',
edgecolors='black', linewidth=1, marker='x')
plt.scatter(class_1[:, 0], class_1[:, 1], s=75, facecolors='white',
edgecolors='black', linewidth=1, marker='o')
plt.title('Input data')

# Split data into training and testing datasets
X_train, X_test, y_train, y_test = model_selection.train_test_split(
X, y, test_size=0.25, random_state=5)


# Decision Trees classifier
params = {'random_state': 0, 'max_depth': 4}
classifier = DecisionTreeClassifier(**params)
classifier.fit(X_train, y_train)
visualize_classifier(classifier, X_train, y_train, 'Training dataset')

y_test_pred = classifier.predict(X_test)
visualize_classifier(classifier, X_test, y_test, 'Test dataset')

# Evaluate classifier performance
class_names = ['Class-0', 'Class-1']
print("\n" + "#"*40)
print("\nClassifier performance on training dataset\n")
print(classification_report(y_train, classifier.predict(X_train),
target_names=class_names))
print("#"*40 + "\n")
print("#"*40)
print("\nClassifier performance on test dataset\n")
print(classification_report(y_test, y_test_pred,
target_names=class_names))
print("#"*40 + "\n")
plt.show()

```
# Results
![image](https://user-images.githubusercontent.com/84629235/149491994-1d9441ab-ec3f-44f4-9bef-cda3059c1ad8.png)

![image](https://user-images.githubusercontent.com/84629235/149492028-a138398e-a253-4fcb-bd17-d64484c04fbc.png)

![image](https://user-images.githubusercontent.com/84629235/149492142-18d6d7e2-5e9f-4b60-a8f9-5483e393d0d4.png)

![image](https://user-images.githubusercontent.com/84629235/149492198-adf5cd10-db5b-45cc-a511-eba2c4d147da.png)



