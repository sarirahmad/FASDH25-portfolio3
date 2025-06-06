#import necessary libraries 
import pandas as pd

#loading the csv file
df = pd.read_csv("data/title.csv")

#print the first 10 rows to inspect the data
print(df.head(10))
