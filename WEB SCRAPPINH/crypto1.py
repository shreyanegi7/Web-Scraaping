from bs4 import BeautifulSoup
import requests


def indent_(value):
    crypto_data = ''
    while value > 0:
        crypto_data += ' '
        value -= 1
    return crypto_data


def profit_loss(market):
    crypto_data = ''
    if market.find('span', class_='sc-15yy2pl-0 hzgCfk'):
        crypto_data += '- ' + market.find('span').text
    else:
        crypto_data += '+ ' + market.find('span').text
    return crypto_data


# Main
url = 'https://coinmarketcap.com/'
response = requests.get(url).text
page_content = BeautifulSoup(response, 'html.parser')

content = page_content.tbody
content_individual = content.contents

print('\n\n\n\n  -|-|-|-|-|------|-|-|-  Crypto  Web-Scraper Using Python --|-|-|-----|-|-|-|-|-\n')
print('````````````````````````````````````````````````````````````````````````````````````````````')
print('\n\t' + page_content.title.string)
print('\n\t\t\tExtacting Data from: ' + url + '\n')

print('````````````````````````````````````````````````````````````````````````````````````````````')
print('\t  Rank\tCrypto\t\tPrice\t\t24-Hr\t  7-Day\t\tMarket-Cap\n')

try:
    for content_indiv in content_individual:
        rank, name, price, market24h, market7d, marketcap = content_indiv.contents[1:7]
        crypto_data = '\t   ' + rank.p.string + '\t' + name.p.string + indent_(
            9 - len(name.p.string)) + '\t' + price.span.string
        crypto_data += indent_(14 - len(price.span.string)) + profit_loss(market24h) + '\t' + profit_loss(
            market7d) + '         ' + marketcap.span.text
        print(crypto_data)

except ValueError:
    print('\n\n````````````````````````````````````````````````````````````````````````````````````````````\n\n')

'''
    Requirements -

    Python Enviroment
    BeautifulSoup Module    ( pip install bs4 )
    Request module          ( pip install requests )


'''