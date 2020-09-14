# import urllib.request, urllib.parse, urllib.error
# import ssl
# import requests as req
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

# Reading locally extracted HTML file
with open("facturen.html", "r") as f:
    contents = f.read()

    # Feed page into bs4
    soup = BeautifulSoup(contents, 'lxml')
    #tags = soup.select('table')
    #info = soup.select('td')
    info = soup.select('span')
    sign = '¬'

    # write a new csv file if it doesnt exist and append to it
    with open('facturen.csv', 'a', newline='') as csvfile:
        datafile = csv.writer(csvfile)
        datafile.writerow(["bedrag"])   # create headers
        for money in info:             # check for symbol in soup
            text = money.get_text()
            if sign in text:            # write selected data to csv
                text1 = text[4:]
                datafile.writerow([text1])

# Testing pandas dataframe calculations

# the decimal parameter is needed for european numerical notation of decimal numbers.
df = pd.read_csv(r'facturen.csv', decimal=",")
pd.to_numeric(df["bedrag"])
sum1 = df["bedrag"].sum()
print(sum1)
