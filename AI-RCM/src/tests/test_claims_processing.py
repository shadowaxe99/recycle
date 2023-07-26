```python
import unittest
from src.claims_processing import process_claims
from src.models.claims_processing_model import ClaimsProcessingModel
from src.data.claims_data import claims_data

class TestClaimsProcessing(unittest.TestCase):

    def setUp(self):
        self.claims_processing_model = ClaimsProcessingModel()
        self.claims_data = claims_data

    def test_process_claims(self):
        processed_claims = process_claims(self.claims_data, self.claims_processing_model)
        self.assertIsNotNone(processed_claims)
        self.assertIsInstance(processed_claims, list)
        self.assertGreater(len(processed_claims), 0)

        for claim in processed_claims:
            self.assertIn('claim_id', claim)
            self.assertIn('status', claim)
            self.assertIn('errors', claim)

if __name__ == '__main__':
    unittest.main()
```