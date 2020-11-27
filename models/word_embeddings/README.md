# Results
The train dataset is downsampled to balance the train dataset.

## `mean_word2vec`
Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 1000000 | 0.6155 | 0.6683
Decision Tree | depth = 2, leaf = 2 | 0.5831 | 0.6933
Random Forest | estimators = 21 | 0.5222 | 0.5867
SVM with grid search | C = 100, deg = 3, kernel = poly | 0.5754 | 0.7350

## `doc2vec`
Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 10000 | 0.5172 | 0.5733
Decision Tree | depth = 5, leaf = 3 | 0.4662 | 0.5017
Random Forest | estimators = 17 | 0.5502 | 0.6600
SVM with grid search | C= 1, deg = 4, kernel = poly | 0.5789 | 0.8733

## `lstm_models`
Best model is saved based on lowest val loss.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Corpus trained | Refer to notebook | 0.5714 | 0.4444
Pretrained Word2Vec | Refer to notebook | 0.3636 | 0.2222
Pretrained GloVe | Refer to notebook | 0.6957 | 0.8888