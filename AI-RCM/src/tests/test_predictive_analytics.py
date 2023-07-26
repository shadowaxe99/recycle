```python
import unittest
from src.predictive_analytics import predict_revenue
from src.data.revenue_data import revenue_data
from src.models.predictive_analytics_model import PredictiveAnalyticsModel

class TestPredictiveAnalytics(unittest.TestCase):

    def setUp(self):
        self.model = PredictiveAnalyticsModel()
        self.data = revenue_data

    def test_predict_revenue(self):
        predictions = predict_revenue(self.data, self.model)
        self.assertIsNotNone(predictions)
        self.assertIsInstance(predictions, list)
        self.assertTrue(all(isinstance(p, float) for p in predictions))

    def test_model_training(self):
        self.model.train(self.data)
        self.assertTrue(self.model.is_trained)

    def test_model_prediction(self):
        self.model.train(self.data)
        predictions = self.model.predict(self.data)
        self.assertIsNotNone(predictions)
        self.assertIsInstance(predictions, list)
        self.assertTrue(all(isinstance(p, float) for p in predictions))

if __name__ == '__main__':
    unittest.main()
```