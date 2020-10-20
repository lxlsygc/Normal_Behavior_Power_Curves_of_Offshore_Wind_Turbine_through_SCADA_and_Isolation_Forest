#Check the wind power curve after resampling

import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt

mpl.rcParams['agg.path.chunksize'] = 100000
pd.options.display.width = 0

df = pd.read_csv("combined_10min_filter1.csv")

df.plot(kind="scatter", x='WindSpeed_mps', y='Power_kW', figsize=(8, 8), color='green')
plt.xlabel('Wind Speed, m/s')
plt.ylabel('Active Power, kW')
plt.savefig('results/speed_vs_power_10min_filter1.png', format="PNG")


