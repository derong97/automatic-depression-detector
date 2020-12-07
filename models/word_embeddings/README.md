# Results

## `mean_word2vec`

### Without undersampling

Best Model | Parameters | val f1
:-----: | :-----: | :-----:
Logistic Regression | C = 1000000 | 0.4543
Decision Tree | depth = 6, leaf = 3 | 0.3595
Random Forest | estimators = 15 | 0.2562
SVM with grid search | C = 100, deg = 5, kernel = poly | 0.4128

### With undersampling

Best Model | Parameters | val f1
:-----: | :-----: | :-----:
Logistic Regression | C = 100 | 0.6225
Decision Tree | depth = 1 | 0.6538
Random Forest | estimators = 17 | 0.5773
SVM with grid search | C = 10, kernel = linear | 0.6041