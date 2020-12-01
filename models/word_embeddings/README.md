# Results
The train dataset is downsampled to balance the train dataset.

## `lstm_models`
Best model is saved based on lowest val loss.

Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----:
Corpus trained | Refer to notebook | 0.6923 | 1.000
Pretrained Word2Vec | Refer to notebook | 0.5000 | 0.4444
Pretrained GloVe | Refer to notebook | 0.5333 | 0.2222