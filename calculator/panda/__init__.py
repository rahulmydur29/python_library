# my_library/__init__.py

from .pde import my_function
import pandas as pd

# Conditional statement to use my_function
def conditional_usage(data):
    if isinstance(data, pd.DataFrame):
        my_function(data)
    else:
        print("Invalid input. Expected a pandas DataFrame.")

# Additional code in the __init__.py file if needed...
