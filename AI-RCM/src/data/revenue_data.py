```python
import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URI

class RevenueData:
    def __init__(self):
        self.engine = create_engine(DATABASE_URI)
        self.revenue_data = self.load_data()

    def load_data(self):
        query = "SELECT * FROM revenue"
        data = pd.read_sql(query, self.engine)
        return data

    def get_data(self):
        return self.revenue_data

    def update_data(self):
        self.revenue_data = self.load_data()

revenue_data = RevenueData().get_data()
```