# Results
The notebook is located [here](https://colab.research.google.com/drive/1M8qHgCoyi1DEtLNYZrCArhODnpJ3YLj8?usp=sharing): 
The train dataset is downsampled to balance the train dataset.

## `pronouns`

Best model is saved based on highest val f1 score.

### Normal sampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 100 | 0.0891 | 0.0656
Decision Tree | depth = 1, leaf = 13, splitter = best | 0.3002 | 0.3242
Random Forest | estimators = 1 | 0.2866 | 0.2923
SVM with grid search | C = 10, kernel = linear | 0.2332 | 0.1937

### Undersampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 100 | 0.3929 | 0.3761
Decision Tree | depth = 1, leaf = 22 | 0.6151 | 0.7051
Random Forest | estimators = 5 | 0.5614 | 0.5848
SVM with grid search | C = 10, kernel = linear | 0.6041 | 0.6994




