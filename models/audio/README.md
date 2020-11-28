# Results
**NOTE**: Some participants are removed from the audio model because the audios have too much (loud) static.
Removed participants: [300, 305, 306, 308, 315, 316, 343, 354, 362, 375, 378, 381, 382, 385, 387, 388, 390, 392, 393, 395, 408, 413, 421, 438, 473, 476, 479, 490, 492]
The models are trained with features that are extracted by 2 different libraries: **Librosa** and **PyAudioAnalysis**

## Librosa Features
Best model is saved based on highest val f1 score.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Gaussian Naive Bayes | NIL | 0.3174 | 0.2951
Logistic Regression | C = 1000 | 0.2300 | 0.2314
Decision Tree | depth = 4, leaf = 5 | 0.4411 | 0.4606
Random Forest | estimators = 1 | 0.3202 | 0.3711
SVM with grid search | C = 100, kernel = linear | 0.2305 | 0.2208

## PyAudioAnalysis Features
Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Gaussian Naive Bayes | NIL | 0.3442 | 0.3692
Logistic Regression | C = 100000 | 0.2847 | 0.2735
Decision Tree | depth = 4, leaf = 3 | 0.3322 | 0.3165
Random Forest | estimators = 7 | 0.2314 | 0.1924
SVM with grid search | C = 100, kernel = linear | 0.2033 | 0.1799