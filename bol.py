# import urllib.request, urllib.parse, urllib.error
# import ssl
import pandas as pd
from bs4 import BeautifulSoup
#import requests as req
import csv


# Reading locally extracted HTML file

with open("facturen.html", "r") as f:
    contents = f.read()

    # Feed page into bs4
    soup = BeautifulSoup(contents, 'lxml')
    tags = soup.select('table')
    info = soup.select('td')
    info2 = soup.select('span')
    info1 = soup.get_text(strip=True)
    money = '€'
    sign = '¬'

    # write a new csv file if it doesnt exist and append to it

    with open('facturen.csv', 'a', newline='') as csvfile:
        datafile = csv.writer(csvfile)
        datafile.writerow(["bedrag"])   # create headers
        for money in info2:             # check for symbol in soup
            text = money.get_text()
            if sign in text:            # write selected data to csv
                text1 = text[4:]
                datafile.writerow([text1])

# Testing pandas dataframe calculations

df = pd.read_csv(r'facturen.csv')

print(df.head())
