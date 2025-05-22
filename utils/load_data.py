import os
import pandas as pd

path = './data/raw/stocks'

data = []
for filename in os.listdir(path):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(path, filename))
        df['Ticker'] = filename.replace('.csv', '')  # Add source ticker
        data.append(df)

combined_df = pd.concat(data, ignore_index=True)