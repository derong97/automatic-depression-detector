# Results
The train dataset is downsampled to balance the train dataset.

## `bag_of_words`
Added Gaussian Naive Bayes model as the baseline model for comparison. BOW is often used with spam text classification.

Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----: |
Gaussian Naive Bayes | NIL | 0.4147 | 0.5217
Logistic Regression | C = 1000000 | 0.6372 | 0.6883
Decision Tree | depth = 3, leaf = 12 | 0.5625 | 0.5750
Random Forest | estimators = 29 | 0.5294 | 0.4833
SVM with grid search | C = 1, deg = 5, kernel = poly | 0.5788 | 0.7367