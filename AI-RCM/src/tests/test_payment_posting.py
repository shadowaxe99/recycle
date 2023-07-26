```python
import unittest
from AI_RCM.src.payment_posting import post_payments
from AI_RCM.src.models.payment_posting_model import PaymentPostingModel
from AI_RCM.src.data.payment_data import payment_data

class TestPaymentPosting(unittest.TestCase):

    def setUp(self):
        self.payment_posting_model = PaymentPostingModel()
        self.payment_data = payment_data

    def test_post_payments(self):
        result = post_payments(self.payment_data, self.payment_posting_model)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('success', result)
        self.assertTrue(result['success'])

if __name__ == '__main__':
    unittest.main()
```