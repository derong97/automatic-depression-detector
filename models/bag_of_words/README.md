# Results
1. The train dataset is balanced and upsampled through paraphrasing.
2. The presented validation f1 and recall scores are the mean of the k-cross validation results.

## `bag_of_words`

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----: |
Logistic Regression | C = 1000000 | 0.8112 | 0.8013
Decision Tree | depth = 4, leaf = 24 | 0.7086 | 0.7199
Random Forest | estimators = 9 | 0.7969 | 0.7649
SVM with grid search | C = 100, gamma = 0.0001, kernel = rbf | 0.7826 | 0.78