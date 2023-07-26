```python
import pandas as pd
from models.claims_processing_model import ClaimsProcessingModel
from utils import clean_data

class ClaimsProcessing:
    def __init__(self, claims_data):
        self.claims_data = claims_data
        self.model = ClaimsProcessingModel()

    def load_data(self):
        # Load claims data
        self.claims_data = pd.read_csv(self.claims_data)

    def preprocess_data(self):
        # Clean and preprocess data
        self.claims_data = clean_data(self.claims_data)

    def process_claims(self):
        # Process claims using AI model
        processed_claims = self.model.predict(self.claims_data)
        return processed_claims

    def save_processed_claims(self, processed_claims):
        # Save processed claims to a csv file
        processed_claims.to_csv('processed_claims.csv', index=False)

if __name__ == "__main__":
    claims_processing = ClaimsProcessing('claims_data.csv')
    claims_processing.load_data()
    claims_processing.preprocess_data()
    processed_claims = claims_processing.process_claims()
    claims_processing.save_processed_claims(processed_claims)
```