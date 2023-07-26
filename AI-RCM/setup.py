```python
from setuptools import setup, find_packages

setup(
    name='AI-RCM',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/yourusername/AI-RCM',
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='AI Revenue Cycle Management system for healthcare organizations',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'keras',
        'flask',
        'sqlalchemy',
        'psycopg2-binary',
        'pycryptodome'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
```