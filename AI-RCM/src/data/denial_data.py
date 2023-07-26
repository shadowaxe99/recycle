```python
import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URI

class DenialData:
    def __init__(self):
        self.engine = create_engine(DATABASE_URI)
        self.denial_data = self.load_data()

    def load_data(self):
        query = "SELECT * FROM denial_data"
        data = pd.read_sql(query, self.engine)
        return data

    def get_denial_data(self):
        return self.denial_data

    def update_denial_data(self, new_data):
        new_data.to_sql('denial_data', self.engine, if_exists='replace')
        self.denial_data = self.load_data()
```