try:
    import pandas as pd
    pandas_available = True
except ImportError:
    pandas_available = False

if pandas_available:
    from .main import my_pandas_function
