import pandas as pd
import glob

#combine all csv files into one csv file
files = glob.glob('*.csv')

combined_csv = pd.concat([pd.read_csv(file, usecols=['WindSpeed_mps','TimeStamp','ActiveAlarm9','Pitch_Deg',
                                           'SubPtchRate1','SubPtchRate2','SubPtchRate3',
                                           'SubPtchPosition3','SubPtchPosition2',
                                        'SubPtchPosition1', 'SubPtchPrivMainShaftSurfTemp', 'Power_kW']) for file in files])

combined_csv.to_csv('combined_1s.csv', index=False)
