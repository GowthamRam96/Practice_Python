# Creating a training pipeline
Machine-learning systems are usually built using different modules. These modules are
combined in a particular way to achieve an end goal. The scikit-learn library has functions
that enable us to build these pipelines by concatenating various modules together. We just need
to specify the modules along with the corresponding parameters. It will then build a pipeline
using these modules that processes the data and trains the system.
The pipeline can include modules that perform various functions like feature selection,
preprocessing, random forests, clustering, and so on. In this section, we will see how to build a
pipeline to select the top K features from an input data point and then classify them using an
Extremely Random Forest classifier.

# Code
```py
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline
from sklearn.ensemble import ExtraTreesClassifier

# Generate data
X, y = samples_generator.make_classification(n_samples=150,n_features=25, n_classes=3, n_informative=6,n_redundant=0, random_state=7)


# Select top K features
k_best_selector = SelectKBest(f_regression, k=9)


# Initialize Extremely Random Forests classifier
classifier = ExtraTreesClassifier(n_estimators=60, max_depth=4)

# Construct the pipeline
processor_pipeline = Pipeline([('selector', k_best_selector), ('erf',
classifier)])

# Set the parameters
processor_pipeline.set_params(selector__k=7, erf__n_estimators=30)

# Training the pipeline
processor_pipeline.fit(X, y)

# Predict outputs for the input data
output = processor_pipeline.predict(X)
print("\nPredicted output:\n", output)

# Print scores
print("\nScore:", processor_pipeline.score(X, y))

# Print the features chosen by the pipeline selector
status = processor_pipeline.named_steps['selector'].get_support()
# Extract and print indices of selected features
selected = [i for i, x in enumerate(status) if x]
print("\nIndices of selected features:", ', '.join([str(x) for x in
selected]))


```

# Results
![image](https://user-images.githubusercontent.com/84629235/158066311-1fa39e0e-4298-449d-9fd2-344943b07bb1.png)
