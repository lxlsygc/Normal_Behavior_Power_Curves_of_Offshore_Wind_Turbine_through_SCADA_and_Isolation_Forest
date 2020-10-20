import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

mpl.rcParams['agg.path.chunksize'] = 100000
pd.options.display.width = 0

#outliers_fraction
outliers_fraction = 0.03

#Load resampled SCADA database
df = pd.read_csv("combined_10min_filter1.csv")

#fill missing data with mean values
df.fillna(df.mean(), inplace=True)

#data extraction
data = df[['WindSpeed_mps', 'Power_kW']]   #,'Pitch_Deg',
                                           #'SubPtchRate1','SubPtchRate2','SubPtchRate3',
                                           #'SubPtchPosition3','SubPtchPosition2',
                                        #'SubPtchPosition1', 'SubPtchPrivMainShaftSurfTemp'

scaler = StandardScaler()
np_scaled = scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)

#train the isolation forest model
model = IsolationForest(contamination=outliers_fraction)

#fit model
model.fit(data)

#1 is representing normal，-1 is representing anomaly
df['anomaly'] = pd.Series(model.predict(data))

#plot outliers vs normal data
fig, ax = plt.subplots(figsize=(8, 8))
a = df.loc[df['anomaly'] == -1, ['WindSpeed_mps', 'Power_kW']] #anomaly value
ax.plot(df['WindSpeed_mps'], df['Power_kW'], color='blue', label='normal')
ax.scatter(a['WindSpeed_mps'], a['Power_kW'], color='red', label='anomaly')
ax.set_xlabel('Wind Speed, m/s')
ax.set_ylabel('Active Power, kW')
plt.legend()
plt.savefig('results/anomaly_vs_normal_IF_{}.png'.format(outliers_fraction), format="PNG")

#plot wind power curve after isolation forest treatment
df = df[df['anomaly'] == 1]
df.plot(kind="scatter", x='WindSpeed_mps', y='Power_kW', alpha=0.1, figsize=(8, 8), color='green')
plt.savefig('results/speed_vs_power_after_filter2_{}.png'.format(outliers_fraction), format="PNG")

#save the updated database
df.to_csv("combined_10min_filter1_filter2_{}.csv".format(outliers_fraction))