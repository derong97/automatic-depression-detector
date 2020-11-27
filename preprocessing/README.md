# README

Note that the following files have been removed due to excluded sessions, interruptions during interview or missing / incomplete transcript
* 342, 373, 394, 398, 402, 416, 417, 444, 451, 458, 460, 480

## Why paraphrasing is not used eventually
Paraphrasing does not change the bulk of the text but mostly replace the original word with synonyms. In our approach, we use k-cross validation due to small dataset. After testing, we realize that the models tend to be overfitted with very high validation scores because in each fold, the train set is likely being evaluated on the validation set that is similar to itself (especially when using pretrained word embeddings which will produce similar vectors).