import numpy as np
import pandas as pd
import matplotlib as plt
import csv

df = pd.read_csv(r'facturen.csv', decimal=",", delimiter=";")
pd.to_numeric(df["bedrag"])
sum1 = df["bedrag"].sum()
mean1 = df.mean()
max1 = df.max()

# bedragen = df["Bedrag"])

print(sum1)

print(df.dtypes)
