# Results
The notebook is located [here](https://colab.research.google.com/drive/1M8qHgCoyi1DEtLNYZrCArhODnpJ3YLj8?usp=sharing): 
The train dataset is downsampled to balance the train dataset.

## `pronouns`

Best model is saved based on highest val f1 score.

### Normal sampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 1000 | 0.1487 | 0.1136
Decision Tree | depth = 1, leaf = 11, splitter = best | 0.4791 | 0.5222
Random Forest | estimators = 9 | 0.3260 | 0.2622
SVM with grid search | C = 10, kernel = linear | 0.6041 | 0.6994

### Undersampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 100000 | 0.4781 | 0.5154
Decision Tree | depth = 1, leaf = 8, splitter = best | 0.6687 | 0.8666
Random Forest | estimators = 17 | 0.5794 | 0.6282
SVM with grid search | C = 10, kernel = linear | 0.6041 | 0.6994

# Ran again

### Normal sampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 10000 | 0.6642 | 0.6642
Decision Tree | depth = 1, leaf = 11, splitter = best | 0.4791 | 0.5222
Random Forest | estimators = 9 | 0.3260 | 0.2622
SVM with grid search | C = 10, kernel = linear | 0.6041 | 0.6994

### Undersampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 100000 | 0.4781 | 0.5154
Decision Tree | depth = 1, leaf = 8, splitter = best | 0.6687 | 0.8666
Random Forest | estimators = 17 | 0.5794 | 0.6282
SVM with grid search | C = 10, kernel = linear | 0.6041 | 0.6994


