import requests
from bs4 import BeautifulSoup

def get_per(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_per")
    tag = tags[0]
    return float(tag.text)

def get_dividend(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_dvr")
    tag = tags[0]
    return float(tag.text)



# print(get_per('000660'))
# print(get_dividend('000660'))


def get_bitcoin():
    url = "https://www.bithumb.com"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")

    tag = soup.select("assetRealBTC_KRW")[0]
    tag2 = soup.select("assetRealETH_KRW")[0]
    print(int(tag.text))
    print(int(tag2.text))

get_bitcoin()