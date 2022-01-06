#  Predictive Analytics with Ensemble Learning
**Ensemble Learning** refers to the process of building multiple models and then combining them
in a way that can produce better results than individual models. These individual models can be
classifiers, regressors, or anything else that models data in some way. Ensemble learning is
used extensively across multiple fields including data classification, predictive modeling,
anomaly detection, and so on.

When we select a model, the most commonly used procedure is to choose the one with the
smallest error on the training dataset. The problem with this approach is that it will not always
work. The model might get biased or overfit the training data. Even when we compute the
model using cross validation, it can perform poorly on unknown data.

One of the main reasons ensemble learning is so effective is because it reduces the overall risk
of making a poor model selection. This enables it to train in a diverse manner and then perform
well on unknown data. When we build a model using ensemble learning, the individual models
need to exhibit some diversity. This would allow them to capture various nuances in our data;
hence the overall model becomes more accurate.

The diversity is achieved by using different training parameters for each individual model. This
allows individual models to generate different decision boundaries for training data. This means
that each model will use different rules to make an inference, which is a powerful way of
validating the final result. If there is agreement among the models, then we know that the output
is correct.

