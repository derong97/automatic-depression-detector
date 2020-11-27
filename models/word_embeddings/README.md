# Results
1. The train dataset is balanced and upsampled through paraphrasing.
2. The presented validation f1 and recall scores are the mean of the k-cross validation results.

## `mean_word2vec`
Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 10000 | 0.8089 | 0.8299
Decision Tree | depth = 4, leaf = 6 | 0.6845 | 0.6857
Random Forest | estimators = 13 | 0.7316 | 0.6992
SVM with grid search | C = 100, deg = 3, kernel = poly | 0.8029 | 0.8062

## `doc2vec`
Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 1000 | 0.894 | 0.891
Decision Tree | depth = 8 | 0.7161 | 0.7340
Random Forest | estimators = 23 | 0.8164 | 0.7755
SVM with grid search | C= 10, deg = 4, kernel = poly | 0.9705 | 0.9529

## `lstm_models`
Best model is saved based on lowest val loss.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Corpus trained | Refer to notebook | 0.6667 | 0.5200
Pretrained Word2Vec | Refer to notebook | 0.5405 | 0.4000
Pretrained GloVe | Refer to notebook | 0.5714 | 0.4800