```python
import unittest
from src.revenue_insights import generate_revenue_insights
from src.data.revenue_data import revenue_data

class TestRevenueInsights(unittest.TestCase):

    def setUp(self):
        self.revenue_data = revenue_data

    def test_generate_revenue_insights(self):
        insights = generate_revenue_insights(self.revenue_data)
        self.assertIsInstance(insights, dict)
        self.assertIn('total_revenue', insights)
        self.assertIn('average_revenue_per_claim', insights)
        self.assertIn('top_revenue_generating_procedures', insights)

if __name__ == '__main__':
    unittest.main()
```