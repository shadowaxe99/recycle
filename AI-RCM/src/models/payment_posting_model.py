```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

class PaymentPostingModel:
    def __init__(self, payment_data):
        self.payment_data = payment_data
        self.model = RandomForestRegressor()

    def preprocess_data(self):
        # Preprocessing steps like handling missing values, encoding categorical variables, etc.
        # This is a placeholder and will need to be modified based on the actual data
        self.payment_data.fillna(0, inplace=True)

    def split_data(self):
        # Splitting the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.payment_data.drop('amount', axis=1), 
            self.payment_data['amount'], 
            test_size=0.2, 
            random_state=42
        )

    def train_model(self):
        # Training the model
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        # Evaluating the model
        predictions = self.model.predict(self.X_test)
        rmse = np.sqrt(mean_squared_error(self.y_test, predictions))
        return rmse

    def predict_payment(self, new_data):
        # Predicting payment for new data
        return self.model.predict(new_data)
```