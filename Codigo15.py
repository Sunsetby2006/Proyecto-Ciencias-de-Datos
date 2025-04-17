import pandas as pd
import numpy as np

# DataFrame con valores faltantes
data = {'Mate': [87, 92, np.nan, 100,97,95], 'Español': [78,89, np.nan, 87,98,90]}
df = pd.DataFrame(data)

df.fillna(df.mean(), inplace=True)

print(df)
