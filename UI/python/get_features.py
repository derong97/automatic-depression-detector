""" import pickle
clfs2 = [clf_b1, clf_b2, clf_b3, clf_w1, clf_w2, clf_w3, clf_tf, clf_p, clf_g1, clf_gh1]
np.save("y_test_final.npy",y_test) """
""" np.save("y_train_final.npy",y_train)
for index,i in enumerate(X_train_ls):
    np.save(f"X_train_list_final_{index}.npy",i) """
""" for index,model in enumerate(clfs2):
    pickle.dump(model,open(f"../../UI/model_{index}.pkl","wb")) """

import numpy as np
import pandas as pd

X_train_bow = np.load("python/data/X_train_bow.npy")
X_test_bow = np.load("python/data/X_test_bow.npy")

X_train_w = np.load("python/data/X_train_mean_w2v.npy")
X_test_w = np.load("python/data/X_test_mean_w2v.npy")

X_train_d = np.load("python/data/X_train_doc2vec.npy")
X_test_d = np.load("python/data/X_test_doc2vec.npy")

X_train_tf = np.load("python/data/X_train_tfidf.npy")
X_test_tf = np.load("python/data/X_test_tfidf.npy")

X_train_p = np.load("python/data/X_train_pronoun.npy", allow_pickle = True)
X_test_p = np.load("python/data/X_test_pronoun.npy", allow_pickle = True)

# f0
X_train_g0 = np.load("python/data/X_train_g0.npy")
X_test_g0 = np.load("python/data/X_test_g0.npy")

# f1
X_train_g1 = np.load("python/data/X_train_g1.npy")
X_test_g1 = np.load("python/data/X_test_g1.npy")

# fh0
X_train_gh0 = np.load("python/data/X_train_gh0.npy")
X_test_gh0 = np.load("python/data/X_test_gh0.npy")

# fh1
X_train_gh1 = np.load("python/data/X_train_gh1.npy")
X_test_gh1 = np.load("python/data/X_test_gh1.npy")

# f01
X_train_g01 = np.load("python/data/X_train_g01.npy")
X_test_g01 = np.load("python/data/X_test_g01.npy")

# fh0h1
X_train_gh0h1 = np.load("python/data/X_train_gh0h1.npy")
X_test_gh0h1 = np.load("python/data/X_test_gh0h1.npy")

X_train_list = [X_train_bow, X_train_bow, X_train_bow, X_train_w, X_train_w, X_train_w, X_train_tf, X_train_p, X_train_g1, X_train_gh1]
X_test_list = [X_test_bow, X_test_bow, X_test_bow, X_test_w, X_test_w, X_test_w, X_test_tf, X_test_p, X_test_g1, X_test_gh1]

#print(X_test_list[0].shape)

y_test = np.load("python/y_test_final.npy")
y_train = np.load("python/y_train_final.npy")
#print(y_test.shape)
#print(X_test_list[0])
#print(y_test)
participant_ids = pd.read_csv("python/test_split_Depression_AVEC2017.csv")['participant_ID'].values

trans = pd.read_csv("python/clean_compiled_transcripts.csv", index_col = "Participant_ID")

def get_particpant_ids(id):
    print("Participant: "+ str(participant_ids[id]))
    return participant_ids[id]

def get_train():
    return X_train_list, y_train

def get_test():

    return X_test_list,y_test

def get_pred(id):

    list_X = []
    list_X.append(X_test_list[id])
    list_Y = []
    list_Y.append(y_test[id])
    
    return list_X,list_Y

def get_trans(id):

    return trans["Transcript"][get_particpant_ids(id)]

#print(participant_ids)