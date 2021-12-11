# Classification
The process of
classification is one such technique where we classify data into a given number of classes.
During classification, we arrange data into a fixed number of categories so that it can be used
most effectively and efficiently.

A good classification system makes it easy to find and retrieve data. This is used extensively in
face recognition, spam identification, recommendation engines, and so on. The algorithms for
data classification will come up with the right criteria to separate the given data into the given
number of classes.

# Pre-Processing data
```py
import numpy as np
from sklearn import preprocessing
input_data = np.array([[5.1, -2.9, 3.3],
[-1.2, 7.8, -6.1],
[3.9, 0.4, 2.1],
[7.3, -9.9, -4.5]])
```
We will be talking about several different preprocessing techniques. Let's start with binarization:
1. Binarization
2. Mean removal
3. Scaling
4. Normalization
Let's take a look at each technique, starting with the first.

# Binarization
```py
# Binarize data
data_binarized =
preprocessing.Binarizer(threshold=2.1).transform(input_data)
print("\nBinarized data:\n", data_binarized)
```
# Output of Binarized Data

Binarized data:
[[ 1. 0. 1.]
[ 0. 1. 0.]
[ 1. 0. 0.]
[ 1. 0. 0.]]

All the values above 2.1 become 1. The remaining values become 0.

# Mean removal

Removing the mean is a common preprocessing technique used in machine learning. It's usually
useful to remove the mean from our feature vector, so that each feature is centered on zero.
We do this in order to remove bias from the features in our feature vector.
```py
# Print mean and standard deviation
print("\nBEFORE:")
print("Mean =", input_data.mean(axis=0))
print("Std deviation =", input_data.std(axis=0))
# Remove mean
data_scaled = preprocessing.scale(input_data)
print("\nAFTER:")
print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", data_scaled.std(axis=0))
```

# Output of Mean Removal

BEFORE:
Mean = [ 3.775 -1.15 -1.3 ]
Std deviation = [ 3.12039661 6.36651396 4.0620192 ]
AFTER:
Mean = [ 1.11022302e-16 0.00000000e+00 2.77555756e-17]
Std deviation = [ 1. 1. 1.]

# Scaling

```py
# Min max scaling
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max scaled data:\n", data_scaled_minmax)
```

# Output of Scaling
Min max scaled data:
[[ 0.74117647 0.39548023 1. ]
[ 0. 1. 0. ]
[ 0.6 0.5819209 0.87234043]
[ 1. 0. 0.17021277]]

# Normalization
We use the process of normalization to modify the values in the feature vector so that we can
measure them on a common scale. In machine learning, we use many different forms of
normalization. Some of the most common forms of normalization aim to modify the values so
that they sum up to 1. L1 normalization, which refers to Least Absolute Deviations, works
by making sure that the sum of absolute values is 1 in each row. L2 normalization, which
refers to least squares, works by making sure that the sum of squares is 1.
In general, L1 normalization technique is considered more robust than L2 normalization
technique. L1 normalization technique is robust because it is resistant to outliers in the data.

```py
# Normalize data
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nL1 normalized data:\n", data_normalized_l1)
print("\nL2 normalized data:\n", data_normalized_l2)
```

# Output for Normalization
L1 normalized data:
[[ 0.45132743 -0.25663717 0.2920354 ]
[-0.0794702 0.51655629 -0.40397351]
[ 0.609375 0.0625 0.328125 ]
[ 0.33640553 -0.4562212 -0.20737327]]
L2 normalized data:
[[ 0.75765788 -0.43082507 0.49024922]
[-0.12030718 0.78199664 -0.61156148]
[ 0.87690281 0.08993875 0.47217844]
[ 0.55734935 -0.75585734 -0.34357152]]
