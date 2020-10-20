import pandas as pd

# Load database
df = pd.read_csv('combined_1s_filter1.csv')

# Set TimeStamp as Index and Resample Data
df.columns = df.columns.get_level_values(0)
df = df.set_index('TimeStamp')
df.index = pd.to_datetime(df.index)
df = df.resample('10T').mean()

#df.fillna(df.mean(), inplace=True)

df.to_csv('combined_10min_filter1.csv')