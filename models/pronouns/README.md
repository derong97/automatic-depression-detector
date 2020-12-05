# Results
The notebook is located [here](https://colab.research.google.com/drive/1M8qHgCoyi1DEtLNYZrCArhODnpJ3YLj8?usp=sharing): 
The train dataset is downsampled to balance the train dataset.

## `pronouns`

Best model is saved based on highest val f1 score.

### Undersampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 100 | 0.3377 | 0.3450
Decision Tree | depth = 1, leaf = 23, splitter = best | 0.6497 | 0.7698
Random Forest | estimators = 17 | 0.5835 | 0.5938
SVM with grid search | C = 10, kernel = linear | 0.6041 | 0.6994


