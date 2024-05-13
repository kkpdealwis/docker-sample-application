import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('../data/car_spending_data.csv')

# Preprocess data
X = data[['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth']]
y = data['Amount Spent for Car']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
with open('../app/model/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

