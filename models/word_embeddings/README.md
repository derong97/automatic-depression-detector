# Results
The train dataset is downsampled to balance the train dataset.

## `mean_word2vec`
Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 100 | 0.6225 | 0.6573
Decision Tree | depth = 1 | 0.6538 | 0.7946
Random Forest | estimators = 17 | 0.5773 | 0.6227
SVM with grid search | C = 10, kernel = linear | 0.6041 | 0.6994

## `doc2vec`
Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 10 | 0.5523 | 0.5770
Decision Tree | depth = 2, leaf = 14 | 0.4971 | 0.4799
Random Forest | estimators = 5 | 0.5532 | 0.5692
SVM with grid search | C= 1, deg = 4, kernel = poly | 0.5950 | 0.8141

## `lstm_models`
Best model is saved based on lowest val loss.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Corpus trained | Refer to notebook | 0.6923 | 1.000
Pretrained Word2Vec | Refer to notebook | 0.5000 | 0.4444
Pretrained GloVe | Refer to notebook | 0.5333 | 0.2222