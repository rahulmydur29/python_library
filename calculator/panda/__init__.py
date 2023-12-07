# my_library/__init__.py

from .pde import MyPandasFunctions
import pandas as pd

class MyPandasLibrary:
    @staticmethod
    def conditional_usage(data):
        if isinstance(data, pd.DataFrame):
            MyPandasFunctions.my_function(data)
        else:
            print("Invalid input. Expected a pandas DataFrame.")
