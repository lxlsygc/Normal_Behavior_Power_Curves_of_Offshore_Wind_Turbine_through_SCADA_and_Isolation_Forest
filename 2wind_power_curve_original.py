import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt

mpl.rcParams['agg.path.chunksize'] = 100000
pd.options.display.width = 0

df = pd.read_csv("combined_1s.csv")

#remove negative wind speed and power

df = df[df['Power_kW'] > 0]
df = df[df['WindSpeed_mps'] > 0]

#plot power curve

df.plot(kind="scatter", x='WindSpeed_mps', y='Power_kW', figsize=(8, 8), color='green')
plt.xlabel('Wind Speed, m/s')
plt.ylabel('Active Power, kW')
plt.savefig('results/speed_vs_power_1s_filter1.png', format="PNG")
df.to_csv('combined_1s_filter1.csv', index=False)
