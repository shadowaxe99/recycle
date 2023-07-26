```python
import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URI

class ClaimsData:
    def __init__(self):
        self.engine = create_engine(DATABASE_URI)
        self.claims_data = self.load_data()

    def load_data(self):
        query = "SELECT * FROM claims"
        data = pd.read_sql(query, self.engine)
        return data

claims_data = ClaimsData().claims_data
```