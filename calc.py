import pandas as pd
import csv
# creating a dataframe that reads in the data

# the decimal parameter is needed for european numerical notation of decimal numbers.
df = pd.read_csv(r'facturen.csv', decimal=",", delimiter=";")
pd.to_numeric(df["bedrag"])
sum1 = df["bedrag"].sum()

print(sum1)
