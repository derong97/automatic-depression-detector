import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
import python.get_features as gf
import os

from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score, \
        f1_score, precision_score, recall_score
import matplotlib.pyplot as plt
from sklearn.base import clone

import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import RepeatedKFold

app = Flask(__name__)
model = pickle.load(open('python/model.pkl','rb'))
model_0 = pickle.load(open('python/model_0.pkl','rb'))
model_1 = pickle.load(open('python/model_1.pkl','rb'))
model_2 = pickle.load(open('python/model_2.pkl','rb'))
model_3 = pickle.load(open('python/model_3.pkl','rb'))
model_4 = pickle.load(open('python/model_4.pkl','rb'))
model_5 = pickle.load(open('python/model_5.pkl','rb'))
model_6 = pickle.load(open('python/model_6.pkl','rb'))
model_7 = pickle.load(open('python/model_7.pkl','rb'))
model_8 = pickle.load(open('python/model_8.pkl','rb'))
model_9 = pickle.load(open('python/model_9.pkl','rb'))

RANDOM_STATE=42
def evaluate_on_training_set(y_test, y_pred):
    # Calculate AUC
    print("AUC is: ", roc_auc_score(y_test, y_pred))

    # print out recall and precision
    print(classification_report(y_test, y_pred))

    # print out confusion matrix
    print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred))

    # # calculate points for ROC curve
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)

    # Plot ROC curve
    plt.plot(fpr, tpr, label='ROC curve (area = %0.3f)' % roc_auc_score(y_test, y_pred))
    plt.plot([0, 1], [0, 1], 'k--')
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')

class Ensemble:
    def __init__(self):
        self.clf = []
        self.X_train = []
        self.X_test = []
        self.y_train = None
        self.y_test = None
        
    def set_clf(self, ls_clf):
        self.clf = ls_clf
    
    def set_train(self, ls_train, y_train):
        self.X_train = ls_train
        self.y_train = y_train
        

    def set_test(self, ls_test, y_test):
        self.X_test = ls_test
        self.y_test = y_test
        

    def train_ens(self):
        for i in range(len(self.clf)):
            c_i = self.clf[i]
            X_train_i = self.X_train[i]
            y_train_i = self.y_train
            c_i.fit(X_train_i, y_train_i)
            self.clf[i] = c_i
        print("Finished Training")   
    
    
    def pred_proba(self, ls_X):
        probas = []
        for i in range(len(self.clf)):
            c_i = self.clf[i]
            probas.append(c_i.predict_proba(ls_X[i]))
        probas = np.array(probas)
        probas = np.mean(probas, axis=0)
        return probas
    
    def pred_ens(self, ls_X):

        probas = self.pred_proba(ls_X)
        label = np.argmax(probas)
        return label
    
    def evaluate_ens(self):
        predictions = []       
        for i in range(len(self.y_test)):
            ls_X = []
            for j in range(len(self.clf)):
                ls_X.append(self.X_test[j][i:i+1][:])
            predictions.append(self.pred_ens(ls_X))
        predictions = np.array(predictions)
        #print(predictions)
        #print(self.y_test)
        return predictions
        
    def ens_kcross(self, k=3, n=4, random_state=RANDOM_STATE):
        f1_scores = []
        recall_scores = []
        rkf = RepeatedKFold(n_splits=k, n_repeats=n, random_state=random_state)
        X = self.X_train[0]
        X_val_ls = []
                
        for train_index, val_index in rkf.split(X):
            
            for i in range(len(self.clf)):
                model = self.clf[i]
                X = self.X_train[i]
                y = self.y_train
                
                X_train, X_val = X[train_index], X[val_index]
                y_train, y_val = y[train_index], y[val_index]

                model.fit(X_train, y_train) 
                
                X_val_ls.append(X_val)
            
                
            predictions = []       
            for i in range(len(y_val)):
                ls_X = []
                for j in range(len(self.clf)):
                    ls_X.append(np.array([X_val_ls[j][i]]))
                pred = self.pred_ens(ls_X)
                predictions.append(pred)
            predictions = np.array(predictions)
            
            f1 = f1_score(y_val, predictions)
            f1_scores.append(f1)
            recall = recall_score(y_val, predictions)
            recall_scores.append(recall)

        return f1_scores, recall_scores

e = Ensemble()
clfs = [model_0,model_1,model_2,model_3,model_4,model_5,model_6,model_7,model_8,model_9]
e.set_clf(clfs)
x_train_list, y_train = gf.get_train()
e.set_train(x_train_list, y_train)
#print(x_train_list[1])
e.train_ens()

@app.route('/')
def home():

    return render_template('index.html',prediction_text='------------------',output2 ='------------------',transcript = "")

@app.route('/predict',methods = ['POST'])
def predict():
    
    
    participant_id = request.form["Participant_ID"]
    participant_id = int(participant_id)
    X_t, y_t = gf.get_test()
    e.set_test(X_t,y_t)
    #X_pred_list, y_pred = gf.get_pred(int(participant_id))
    #print(ls_X)
    prediction = e.evaluate_ens()
    print(prediction)
    
    if prediction[participant_id] == 0:
        text = "not depressed"
    else:
        text = "depressed"
    return render_template('index.html',prediction_text=text)

@app.route('/predict2',methods = ['POST'])
def predict2():
    print(request.form)
    if "predict" in request.form["submit"]:
        participant_id = request.form["Participant_ID"]
        participant_id = int(participant_id)
        X_t, y_t = gf.get_test()
        e.set_test(X_t,y_t)
        #X_pred_list, y_pred = gf.get_pred(int(participant_id))
        #print(ls_X)
        prediction = e.evaluate_ens()
        print(prediction)
        
        if prediction[participant_id] == 0:
            text = "not depressed"
        else:
            text = "depressed"
        return render_template('index.html',prediction_text=text)
    elif "transcript" in request.form["submit"]:
        participant_id = request.form["Participant_ID"]
        participant_id = int(participant_id)
        transcript_final = gf.get_trans(participant_id)

        return render_template('index.html',transcript = transcript_final)
    elif "label" in request.form["submit"]:
        participant_id = request.form["Participant_ID"]
        participant_id = int(participant_id)
        transcript_final = gf.get_trans(participant_id)
        X_t, y_t = gf.get_test()
        if y_t[participant_id] == 0:
            text = "not depressed"
        else:
            text = "depressed"
        return render_template('index.html',output2 = text)

@app.route('/transcript',methods = ['POST'])
def transcript():
    participant_id = request.form["Participant_ID"]
    participant_id = int(participant_id)
    transcript_final = gf.get_trans(participant_id)

    return render_template('index.html',transcript = transcript_final)

@app.route('/label',methods = ['POST'])
def label():
    participant_id = request.form["Participant_ID"]
    participant_id = int(participant_id)
    transcript_final = gf.get_trans(participant_id)
    X_t, y_t = gf.get_test()
    if y_t[participant_id] == 0:
        text = "not depressed"
    else:
        text = "depressed"
    return render_template('index.html',output2 = text)
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True