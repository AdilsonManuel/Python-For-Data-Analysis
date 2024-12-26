import pandas as pd

data = [10, 20, 30, None, 50]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(series)
