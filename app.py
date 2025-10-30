import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    input_data = np.array(list(data.values())).reshape(1, -1)
    new_data = scaler.transform(input_data)
    output = regmodel.predict(new_data)
    return jsonify({'prediction': output[0]})



@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()] 
    final_input = scaler.transform(np.array(data).reshape(1,-1))   
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template('Home.html', prediction_text=f'The predicted House Price is {output}')

if __name__ == "__main__":
    app.run(debug=True)