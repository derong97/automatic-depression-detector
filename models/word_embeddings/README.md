# Results
1. The train dataset is balanced and upsampled through paraphrasing.
2. The presented validation f1 and recall scores are the mean of the k-cross validation results.

## `mean_word2vec`

Best Model | Parameters | val f1 | test f1 | val recall | test recall 
:-----: | :-----: | :-----: | :-----: | :-----: | :-----:
Logistic Regression | C = 10000 | 0.8089 | 0.58 | 0.8299 | 0.64
Decision Tree | depth = 8, leaf = 6 | 0.6845 | 0.34 | 0.6857 | 0.43
Random Forest | estimators = 13 | 0.7316 | 0.10 | 0.7136 | 0.07
SVM with grid search | C = 100, deg = 3, kernel = poly | 0.8029 | 0.57 | 0.8062 | 0.57

## `doc2vec`
Not done.

Best Model | Parameters | val f1 | test f1 | val recall | test recall 
:-----: | :-----: | :-----: | :-----: | :-----: | :-----:
Logistic Regression | 
Decision Tree | 
Random Forest | 
SVM with grid search | 

## `lstm_models`
Not sure how to save the weights based on best f1 score so cannot compare val and test.
- KIV: https://stackoverflow.com/questions/55153983/how-to-save-best-model-in-keras-based-on-auc-metric

Best Model | Parameters | val f1 | test f1 | val recall | test recall 
:-----: | :-----: | :-----: | :-----: | :-----: | :-----:
Corpus trained LSTM |
Pretrained Word2Vec |
Pretrained GloVe |