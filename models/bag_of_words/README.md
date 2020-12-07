# Results

## `bag_of_words`

### Without undersampling
Best Model | Parameters | val f1
:-----: | :-----: | :-----:
Logistic Regression | C = 10000 | 0.4600
Decision Tree | depth = 3, leaf = 18 | 0.3942
Random Forest | estimators = 1 | 0.3248
SVM with grid search | C = 1, kernel = linear | 0.4070

### With undersampling
Best Model | Parameters | val f1
:-----: | :-----: | :-----:
Logistic Regression | C = 1000000 | 0.6440
Decision Tree | depth = 1, leaf = 13 | 0.6473
Random Forest | estimators = 23 | 0.6121
SVM with grid search | C = 10, gamma = 0.001, kernel = rbf | 0.5547