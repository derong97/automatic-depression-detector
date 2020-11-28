# Results
The train dataset is downsampled to balance the train dataset.

## `bag_of_words`
Added Gaussian Naive Bayes model as the baseline model for comparison. BOW is often used with spam text classification.

Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----: |
Gaussian Naive Bayes | NIL | 0.5066 | 0.4925
Logistic Regression | C = 1000000 | 0.6440 | 0.6621
Decision Tree | depth = 1, leaf = 13 | 0.6473 | 0.7275
Random Forest | estimators = 23 | 0.6121 | 0.6449
SVM with grid search | C = 10, gamma = 0.001, kernel = rbf | 0.5547 | 0.6325