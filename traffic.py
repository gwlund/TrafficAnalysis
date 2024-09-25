#read csv file into a pandas dataframe
import pandas as pd

#read the csv file
df = pd.read_csv('WA_Crash_Summary.csv')

#summarize the data
print(df.head())
print(df.info())
print(df.describe())


