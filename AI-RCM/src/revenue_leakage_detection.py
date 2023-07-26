```python
import pandas as pd
from models.revenue_leakage_model import RevenueLeakageModel
from utils import load_data, save_results
from config import revenue_data

def detect_revenue_leakage():
    # Load revenue data
    data = load_data(revenue_data)

    # Initialize the model
    model = RevenueLeakageModel()

    # Train the model
    model.train(data)

    # Predict revenue leakage points
    leakage_points = model.predict(data)

    # Save the results
    save_results(leakage_points, 'revenue_leakage_detection_results.csv')

    return leakage_points

if __name__ == "__main__":
    detect_revenue_leakage()
```