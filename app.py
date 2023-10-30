import numpy as np
from flask import Flask, request, jsonify
from pathlib import Path
import pandas as pd
import joblib


model = joblib.load(Path(__file__).with_name('model.joblib'))

app = Flask(__name__)



#Example post
#http://localhost:5000/?check=foobar123
@app.route('/', methods=['POST'])
def get_prediction():
    

    password = request.form('password') 
    psw = np.array([password])
    
    prediction = model(psw)
    
    
    if prediction == 1:
        result = "Strong password."
    else:
        result = "Weak password."

    return jsonify(result)

app.run(debug=True)