# Confusion matrix
A Confusion matrix is a figure or a table that is used to describe the performance of a
classifier. It is usually extracted from a test dataset for which the ground truth is known. We
compare each class with every other class and see how many samples are misclassified.
During the construction of this table, we actually come across several key metrics that are very
important in the field of machine learning. Let's consider a binary classification case where the
output is either 0 or 1:

**True positives:** These are the samples for which we predicted 1 as the output and the
ground truth is 1 too.

**True negatives:** These are the samples for which we predicted 0 as the output and the
ground truth is 0 too.

**False positives:** These are the samples for which we predicted 1 as the output but the
ground truth is 0. This is also known as a Type I error.

**False negatives:** These are the samples for which we predicted 0 as the output but the
ground truth is 1. This is also known as a Type II error


# code
```py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Define sample labels
true_labels = [2, 0, 0, 2, 4, 4, 1, 0, 3, 3, 3]
pred_labels = [2, 1, 0, 2, 4, 3, 1, 0, 1, 3, 3]

# Create confusion matrix
confusion_mat = confusion_matrix(true_labels, pred_labels)

# Visualize confusion matrix
plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.gray)
plt.title('Confusion matrix')
plt.colorbar()
ticks = np.arange(5)
plt.xticks(ticks, ticks)
plt.yticks(ticks, ticks)
plt.ylabel('True labels')
plt.xlabel('Predicted labels')
plt.show()

# Classification report
targets = ['Class-0', 'Class-1', 'Class-2', 'Class-3', 'Class-4']
print('\n', classification_report(true_labels, pred_labels,
target_names=targets))


```
# Results
![image](https://user-images.githubusercontent.com/84629235/147847837-26445ae4-b4b3-4ac3-9038-7604cee4b1a7.png)

![image](https://user-images.githubusercontent.com/84629235/147847888-3ac7991c-f81c-4618-b044-80a09c8dfe9d.png)


