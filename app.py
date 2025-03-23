import numpy as np
import pickle
import math

from flask import Falsk , request , jsonify , render_template

app = Flask(__name__, template_folder = 'template', static_folder = 'staticfiles') # assign Flask = app
model = pickle.load(open('build.pkl','rb')) # import model

@app.route('/') ## root folder
def home():
    return render_template('index.html') # reading index.html file

@app.route('/predict', methods = ['POST']) ## TRansfer data from html to python/serve

def predict():
    int_features = [int(x) for x in request.form.values()] 
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if prediction == 1:
        return render_template('index.html',prediction_text = "Loan is Rejected").format(prediction)
    else:
        return render_template('index.html',prediction_text = "Loan is Approved").format(prediction)

    if __name__ == __main__:
        app.run(host="0.0.0.0", port = 8080) 