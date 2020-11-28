# Results
1. The train dataset is split into 4 feature vectors:
- f0: (x_0, y_0, z_0)
- f1: (x_1, y_1, z_1) 
- fh0: (x_h0, y_h0, z_h0)
- fh1: (x_h1, y_h1, z_h1)
2. The presented validation f1 and recall scores are the mean of the k-cross validation results.

Best model is saved based on highest val f1 score.

Using k=10, n=1
# Without undersampling
Features | Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----: | :-----:
All | Decision Tree | depth: 8, leaf: 7 | 0.24746 | 0.19857
f0 | Decision Tree | depth: 6, leaf: 6 | 0.35859 | 0.35452
f1 | Decision Tree | depth: 14, leaf: 1 | 0.34081 | 0.34357
fh0 | Decision Tree | depth: 14, leaf: 1 | 0.34081 | 0.34357
fh1 | Random Forest | estimators = 1 | 0.37442 | 0.40286
f0+f1 | Decision Tree | depth: 8, leaf: 6 | 0.32947 | 0.32952
fh0+fh1 | Decision Tree | depth: 8, leaf: 6 | 0.32947 | 0.32952

Using k=4, n=3
# With undersampling
Features | Best Model | Parameters | val f1 | val recall
:-----: | :-----: | :-----: | :-----: | :-----:
All | Decision Tree | depth: 2, leaf: 12 | 0.53982 | 0.59525
f0 | Decision Tree | depth: 2, leaf: 15 | 0.55062 | 0.65431
f1 | Decision Tree | depth: 3, leaf: 12 | 0.60029 | 0.64075
fh0 | Decision Tree | depth: 2, leaf: 18 | 0.52187 | 0.58821
fh1 | Decision Tree | depth: 3, leaf: 14 | 0.64815 | 0.77762
f0+f1 | SVM with grid search | C = 100, kernel = poly, deg = 3 | 0.55401 | 0.72577
fh0+fh1 | Decision Tree | depth: 2, leaf: 13 | 0.54228 | 0.63928
