# Results

## `tfidf`

Best model is saved based on highest val f1 score.

### Without Undersampling
Best Model | Parameters | val f1 
:-----: | :-----: | :-----: | 
Decision Tree | depth = 1, leaf = 24 | 0.5266 
Random Forest | estimators = 1 | 0.3049 
Logistic Regression | C = 1000000 | 0.2952 
SVM with Grid Search| C: 10, kernel: linear | 0.3102 

### Undersampling
Best Model | Parameters | val f1 
:-----: | :-----: | :-----: | 
Decision Tree | depth = 1, leaf = 30 | 0.6121 
Random Forest | estimators = 1 | 0.5502 
Logistic Regression | C = 1000000 | 0.2579 
SVM with Grid Search| C: 10, kernel: linear | 0.6976 
