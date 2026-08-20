import pandas as pd
import numpy as np

data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

df2 = pd.DataFrame(data2)

print("Before filling missing values:")
print(df2)

# Fill Math missing value with Math column mean
df2['Math'] = df2['Math'].fillna(df2['Math'].mean())

# Fill Science missing value with Science column mean
df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

print("\nAfter filling missing values:")
print(df2)