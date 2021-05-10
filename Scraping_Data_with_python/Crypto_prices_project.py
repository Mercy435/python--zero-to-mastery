import requests
from bs4 import BeautifulSoup
import pprint
import json
import pandas as pd
import time

# print(help(pd))
from pandas.io.formats import info

res = requests.get('https://coinmarketcap.com/')
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.title)
# identify which data to extract and scout for where it is in the site
# pprint.pprint(soup.prettify()) #prints page element as a string
# search for where u can get the data: id, symbol,slug and get the class
# print(help(soup))

data = soup.find('script', id="__NEXT_DATA__", type="application/json")
# print(data)  # shows u were the historical data u need is located
# create a dictionary to contain id and slug
coins = {}



# data.contents[0] remove script tags
coin_data = json.loads(data.contents[0])
# print(coin_data)
listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']  # nested json,
# print(listings)

for i in listings:
    coins[str(i['id'])] = i['slug']


# creating a template of needed info
market_cap = []
volume = []
timestamp = []
name = []
symbol = []
slug = []
for i in coins:
    page = requests.get(f'https://coinmarketcap.com/currencies/{coins[i]}/historical-data/?'
                        f'start=20200101&end=20200630)')  # getting data using date
    soup = BeautifulSoup(page.content, 'html.parser')
    # data = soup.find('script', id="__NEXT_DATA__", type="application/json") y was this repeated
    historical_data = json.loads(data.contents[0])
# print(historical_data)
    quotes = historical_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
    # import pprint
    # pprint.pprint(quotes)
    # break

    # sending data from beautifulsoup to arrays and then df
    for j in quotes:
        # pprint.pprint(j)
        # break
        market_cap.append(j['quote']['USD']['marketCap'])
        volume.append(j['quote']['USD']['volume24h'])
        # # timestamp.append(j['quote']['USD']['timestamp'])
        # name.append(info['name'])
        # symbol.append(info['symbol'])
        slug.append(coins[i])

    df = pd.DataFrame(columns=['marketcap', 'volume', 'timestamp', 'name', 'symbol', 'slug'])
    df['marketcap'] = market_cap
    df['volume'] = volume
    # df['timestamp'] = timestamp
    # df['name'] = name
    # df['symbol'] = symbol
    df['slug'] = slug

    # saving as csv
    df.to_csv('criptoes.csv', index=False)
