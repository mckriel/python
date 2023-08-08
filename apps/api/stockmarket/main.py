import requests
import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_KEY = 'AJNV95BGCT41LYTG'
NEWS_KEY = '3ea3c350994442349a3fb3add7ad3e5e'

DATE = datetime.date.today()

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': ALPHA_KEY,
}

news_params = {
    'qInTitle': COMPANY_NAME,
    'apiKey': NEWS_KEY,
}


def get_news():
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    data = response.json()['articles']
    print(f'News articles on {COMPANY_NAME}')
    for article in data[:3]:
        print(f'Title: {article["title"]}')
        print(f'URL: {article["url"]}')


def get_pricing():
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()['Time Series (Daily)']
    data_list = [value for (key, value) in data.items()]

    closing_price_yesterday = data_list[0]['4. close']
    closing_price_day_before = data_list[1]['4. close']
    difference_value = float(closing_price_yesterday) - float(closing_price_day_before)
    difference_percentage = ((float(closing_price_yesterday)/float(closing_price_day_before)) * 100) - 100

    print(f'Company: {COMPANY_NAME} ({STOCK_NAME})')
    print(f'Closing price yesterday: ${closing_price_yesterday}')
    print(f'Closing price day before: ${closing_price_day_before}')
    print(f'Price difference: ${difference_value}')
    print(f'Percentage difference: {difference_percentage}%')

    if difference_percentage >= 5:
        get_news()


get_pricing()
