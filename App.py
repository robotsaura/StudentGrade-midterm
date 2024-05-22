#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
from flask import Flask, request, render_template

# Load the model, scaler, and label encoder
with open('svc_model.pkl', 'rb') as model_file:
    svc_model = pickle.load(model_file)
    
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('label_encoder.pkl', 'rb') as encoder_file:
    label_encoder = pickle.load(encoder_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    math = float(request.form['math'])
    read = float(request.form['read'])
    write = float(request.form['write'])
    
    # Prepare the input data
    input_data = [[math, read, write]]
    scaled_data = scaler.transform(input_data)
    
    # Predict the race category
    prediction = svc_model.predict(scaled_data)
    race_category = label_encoder.inverse_transform(prediction)[0]
    
    return f"The predicted race category is: {race_category}"

if __name__ == '__main__':
    app.run(debug=True)

