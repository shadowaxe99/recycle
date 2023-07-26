```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from cryptography.fernet import Fernet

def clean_data(df):
    """
    Function to clean data
    """
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def encode_data(df):
    """
    Function to encode categorical data
    """
    for column in df.columns:
        if df[column].dtype == type(object):
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
    return df

def generate_encryption_key():
    """
    Function to generate encryption key
    """
    key = Fernet.generate_key()
    return key

def encrypt_data(data, key):
    """
    Function to encrypt data
    """
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """
    Function to decrypt data
    """
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data
```