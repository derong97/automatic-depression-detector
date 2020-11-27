# Results
1. The train dataset is balanced and upsampled through paraphrasing.
2. The presented validation f1 and recall scores are the mean of the k-cross validation results.

## `bag_of_words`
Added Naive Bayes because it is often used together with BOW for spam filtering detection tasks. Will be using it as the baseline for performance comparison.

Best Model | Parameters | val f1 | test f1 | val recall | test recall 
:-----: | :-----: | :-----: | :-----: | :-----: | :-----:
Gaussian Naive Bayes | NIL | 0.9399 | 0.12 | 0.9667 | 0.07
Logistic Regression | C = 1000000 | 0.8112 | 0.53 | 0.8013 | 0.57
Decision Tree | depth = 4, leaf = 24 | 0.7086 | 0.42 | 0.7199 | 0.50
Random Forest | estimators = 9 | 0.77 | 0.29 | 0.7834 | 0.21
SVM with grid search | C = 100, gamma = 0.0001, kernel = rbf | 0.7826 | 0.35 | 0.78 | 0.29