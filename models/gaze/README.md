# Results
1. The train dataset is split into 4 feature vectors:
- f0: (x_0, y_0, z_0)
- f1: (x_1, y_1, z_1) 
- fh0: (x_h0, y_h0, z_h0)
- fh1: (x_h1, y_h1, z_h1)
2. The presented validation f1 and recall scores are the mean of the k-cross validation results.

Best model is saved based on highest val f1 score.

# Without undersampling
Features | Best Model | Parameters | val f1 
:-----: | :-----: | :-----: | :-----: 
All | Decision Tree | depth: 7, leaf: 10 | 0.28608 
f0 | Decision Tree | depth: 8, leaf: 4 | 0.27309 
f1 | Decision Tree | depth: 10, leaf: 1 | 0.32256 
fh0 | Decision Tree | depth: 11, leaf: 1 | 0.35291 
fh1 | Decision Tree | depth: 10, leaf: 3 | 0.22051 
f0+f1 | Decision Tree | depth: 13, leaf: 1 | 0.30106 
fh0+fh1 | Decision Tree | depth: 9, leaf: 5 | 0.28877 

# With undersampling
Features | Best Model | Parameters | val f1 
:-----: | :-----: | :-----: | :-----: 
All | Decision Tree | depth: 2, leaf: 12 | 0.53982
f0 | Decision Tree | depth: 2, leaf: 15 | 0.55062 
f1 | Decision Tree | depth: 3, leaf: 12 | 0.60029 
fh0 | Decision Tree | depth: 2, leaf: 18 | 0.52187 
fh1 | Decision Tree | depth: 3, leaf: 14 | 0.64815 
f0+f1 | SVM with grid search | C = 100, kernel = poly, deg = 3 | 0.55401 
fh0+fh1 | Decision Tree | depth: 2, leaf: 13 | 0.54228 
