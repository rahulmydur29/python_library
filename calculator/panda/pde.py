# my_library/pd.py

import pandas as pd

class MyPandasFunctions:
    @staticmethod
    def my_function(data):
        if isinstance(data, pd.DataFrame):
            # Perform some action on the DataFrame
            # For example, print the first few rows
            print(data.head())
        else:
            print("Input is not a pandas DataFrame")
