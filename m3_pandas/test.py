import pandas as pd
import numpy as np


data1 = ['PandasAll', 123.1, 123123, 11]
print(pd.Series(data1, index=['первый', 'второй', 'третий', 'пятый']))

n = {'a': 1, 'b': 2, 'c': 3}
print(pd.Series(n))
