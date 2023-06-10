from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import api

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_stock_price():
    url = STOCK_ENDPOINT
    parameters = {
        'function': 'TIME_SERIES_WEEKLY',
        'symbol': STOCK_NAME,
        'apikey': api.stockapikey,
    }
    session = Session()
    try:
        response = session.get(url=url, params=parameters)
        print(f'Query URL: {response.request.url}')
        data = response.json()
        for week_data in data['Weekly Time Series']:
            open_price = float(data['Weekly Time Series'][week_data]['1. open'])
            close_price = float(data['Weekly Time Series'][week_data]['4. close'])
            variance = calculate_variance(float(open_price), float(close_price))
            print(f'Week: {week_data} | Open price: ${format_float(open_price)} | Close price: ${format_float(close_price)} | Variance: {format_float(variance)}%')
            # print(open_price, close_price)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def calculate_variance(open_price: float, close_price: float) -> float:
    return 100 - ((open_price / close_price) * 100)


def format_float(float_input: float) -> str:
    return str("{:,.2f}".format(round(float_input, 2)))


get_stock_price()


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").




#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

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

