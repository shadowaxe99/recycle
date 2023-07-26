```python
import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URI

class PaymentData:
    def __init__(self):
        self.engine = create_engine(DATABASE_URI)
        self.payment_data = self.load_data()

    def load_data(self):
        query = "SELECT * FROM payment_data"
        data = pd.read_sql(query, self.engine)
        return data

    def get_data(self):
        return self.payment_data

payment_data = PaymentData().get_data()
```