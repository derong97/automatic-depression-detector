import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
import python.get_features
import os

app = Flask(__name__)
model = pickle.load(open('python/model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html',prediction_text='------------------')

@app.route('/predict',methods = ['POST'])
def predict():
    
    participant_id = request.form["Participant_ID"]
    X_test, y_test = python.get_features.get(int(participant_id))
    prediction = model.predict(X_test.reshape(1,-1))
    
    if prediction == 0:
        text = "not depressed"
    else:
        text = "depressed"
    return render_template('index.html',prediction_text='The participant is predicted as {}, the y test is {}'.format(text,y_test))

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