# Label Encoding
When we perform classification, we usually deal with a lot of labels. These labels can be in the
form of words, numbers, or something else. The machine learning functions in sklearn expect
them to be numbers. So if they are already numbers, then we can use them directly to start
training. But this is not usually the case.
In the real world, labels are in the form of words, because words are human readable. We
label our training data with words so that the mapping can be tracked. To convert word labels
into numbers, we need to use a label encoder. Label encoding refers to the process of
transforming the word labels into numerical form. This enables the algorithms to operate on our
data.


```py
import numpy as np
from sklearn import preprocessing

# Sample input labels
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

# Create label encoder and fit the labels
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

# Print the mapping
print("\nLabel mapping:")
for i, item in enumerate(encoder.classes_):
    print(item, '-->', i)

# Encode a set of labels using the encoder
test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels)
print("Encoded values =", list(encoded_values))

# Decode a set of values using the encoder
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("Decoded labels =", list(decoded_list))

```

# Result of Above code
```
Label mapping:
black --> 0
green --> 1
red --> 2
white --> 3
yellow --> 4

Labels = ['green', 'red', 'black']
Encoded values = [1, 2, 0]

Encoded values = [3, 0, 4, 1]
Decoded labels = ['white', 'black', 'yellow', 'green']
```
