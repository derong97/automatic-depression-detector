# Results
The notebook is located [here](https://colab.research.google.com/drive/1dXMdHlRfphgNBBIoqCJ7XH4xLjt1Vftk?usp=sharing): 
The train dataset is downsampled to balance the train dataset.

## `tfidf`
Added Multinomial Naive Bayes model as the baseline model for comparison. 

Best model is saved based on highest val f1 score.

### Without Undersampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----: |
Decision Tree | depth = 1, leaf = 30 | 0.4836 | 0.5783
Random Forest | estimators = 1 | 0.3446 | 0.3047
Logistic Regression | C = 1000000 | 0.3988 | 0.3079
SVM with Grid Search| C: 10, kernel: linear | 0.4017 | 0.3153

### Undersampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----: |
Decision Tree | depth = 1, leaf = 30 | 0.6121 | 0.6422
Random Forest | estimators = 5 | 0.5439 | 0.5747
Logistic Regression | C = 10000 | 0.1185 | 0.0890
SVM with Grid Search| C: 10, kernel: linear | 0.6976 | 0.7123


