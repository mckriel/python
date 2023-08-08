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
    difference_percentage = 7 #((float(closing_price_yesterday)/float(closing_price_day_before)) * 100) - 100

    print(f'Company: {COMPANY_NAME} ({STOCK_NAME})')
    print(f'Closing price yesterday: ${closing_price_yesterday}')
    print(f'Closing price day before: ${closing_price_day_before}')
    print(f'Price difference: ${difference_value}')
    print(f'Percentage difference: {difference_percentage}%')

    if difference_percentage >= 5:
        get_news()


get_pricing()


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

