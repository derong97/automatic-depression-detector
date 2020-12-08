# Results
**NOTE**: Some participants are removed from the audio model because the audios have too much (loud) static.
Removed participants: [300, 305, 306, 308, 315, 316, 343, 354, 362, 375, 378, 381, 382, 385, 387, 388, 390, 392, 393, 395, 408, 413, 421, 438, 473, 476, 479, 490, 492]
The models are trained with features that are extracted by 2 different libraries: **Librosa** and **PyAudioAnalysis**

## Librosa Features
Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1
:-----: | :-----: | :-----:
Gaussian Naive Bayes | NIL | 0.3174
Logistic Regression | C = 1000 | 0.2300
Decision Tree | depth = 4, leaf = 5 | 0.4411
Random Forest | estimators = 1 | 0.3202
SVM with grid search | C = 100, kernel = linear | 0.2305

## PyAudioAnalysis Features
Best Model | Parameters | val f1
:-----: | :-----: | :-----:
Gaussian Naive Bayes | NIL | 0.3442
Logistic Regression | C = 100000 | 0.2847
Decision Tree | depth = 4, leaf = 3 | 0.3322
Random Forest | estimators = 7 | 0.2314
SVM with grid search | C = 100, kernel = linear | 0.2033
