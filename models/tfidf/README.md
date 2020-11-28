# Results
The notebook is located [here](https://colab.research.google.com/drive/1dXMdHlRfphgNBBIoqCJ7XH4xLjt1Vftk?usp=sharing): 
The train dataset is downsampled to balance the train dataset.

## `tfidf`
Added Multinomial Naive Bayes model as the baseline model for comparison. 

Best model is saved based on highest val f1 score.

### Undersampling
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----: |
Multinomial Naive Bayes | alpha = 0.5 | 0.5272 | 0.6383
Logistic Regression | C = 10000 | 0.0666 | 0.0533
AdaBoost Classifier | n_estimators = 1000, learning_rate = 0.1 | 0.52772 | 0.5050
SVM with Grid Search| C: 10, kernel: linear | 0.6441 | 0.7583


