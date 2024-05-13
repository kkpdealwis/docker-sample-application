from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        country = request.form['country']
        gender = request.form['gender']
        age = float(request.form['age'])
        annual_salary = float(request.form['annual_salary'])
        credit_card_debt = float(request.form['credit_card_debt'])
        net_worth = float(request.form['net_worth'])

        input_features = np.array([[age, annual_salary, credit_card_debt, net_worth]])
        prediction = model.predict(input_features)[0]

        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
