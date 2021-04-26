import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://www.blockchain.com/btc/address/39qrdxFmkP3bC7Qe74wE4VXemQzXzNHr1h?page=3')
soup = BeautifulSoup(res.text, 'html.parser')
hash_ = soup.select('.sc-1r996ns-0.fLwyDF.sc-1tbyx6t-1.kCGMTY.iklhnl-0.eEewhk')


def scraped_hash(h):
    return h.text


a = list(map(scraped_hash, hash_))
# print(len(a[0]))
result1 = [item for item in a if len(item) == 64]
# print(result1)
# alternatively,
# while '' in a:
# a.remove('')
# pprint.pprint(a[0::2])
# date = soup.select('.sc-1ryi78w-0.cILyoi.sc-16b9dsl-1.ZwupP.u3ufsr-0.eQTRKC')
date = soup.select('.kad8ah-0.fjudWa')  # using the parent class,div
# pprint.pprint(date)
result2 = [item.getText() for item in date]


# pprint.pprint(result_)
# print(result2)


def scraped_date(d):  # using the class child span
    return d.text


# b = list(map(scraped_date, date))
# print(b)
# result_ = [item for item in b if '2021' in item]
# print(result_)
btc = soup.select('.kad8ah-0.drlFvR')
# pprint.pprint(btc)
# result = [item.getText()for item in btc]
# to remove ' BTC'
result3 = [item.getText().replace(' BTC', '') for item in btc]


# print(result3)

def create_custom_cl(*arg):
    compiled_list = []
    for index, item in enumerate(result1):
        link_hash = result1[index]
        datetime = result2[index]
        _BTC = result3[index]
        compiled_list.append({'hash': link_hash, 'datetime': datetime, 'BTC': _BTC})

    return compiled_list


pprint.pprint(create_custom_cl(result1, result2, result3))
