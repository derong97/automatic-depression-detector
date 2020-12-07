# Results

## `doc2vec`

### Without undersampling

Best Model | Parameters | val f1
:-----: | :-----: | :-----:
Logistic Regression | C = 100000 | 0.4022
Decision Tree | depth = 7, leaf = 4 | 0.2806
Random Forest | estimators = 1 | 0.3894
SVM with grid search | C = 1, kernel = linear | 0.3765

### With undersampling

Best Model | Parameters | val f1
:-----: | :-----: | :-----:
Logistic Regression | C = 1000000 | 0.5147
Decision Tree | depth = 1, leaf = 20 | 0.5478
Random Forest | estimators = 21 | 0.5993
SVM with grid search | C= 1, deg = 4, kernel = poly | 0.5830