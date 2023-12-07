import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_KEY")
STOCK_API_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWSAPI_KEY")

TWILLO_SID = os.environ.get("TWILLO_SID")
TWILLO_AUTH_TOKEN = os.environ.get("TWILLO_AUTH_TOKEN")

# getting the stock data
stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_API_PARAMS)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

# getting the yesterday's closing price
price_list = [value for (key, value) in stock_data.items()]
yesterday_closing_price = float(price_list[0]["4. close"])

# getting the day before yesterday's closing price
day_before_yesterday_closing_price = float(price_list[1]["4. close"])

# difference between
# yesterday's closing price and day before yesterday's closing price
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# percentage difference between
# yesterday's closing price and day before yesterday's closing price
diff_percent = round((difference / yesterday_closing_price) * 100)

# if the percentage difference is greater than 5 then get the news articles
if abs(diff_percent) > 5:
    NEWS_API_PARAMS = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "language": "en"
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_API_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    news_articles = news_data[:3]

    articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%"
                "\nHeadline: {article['title']}."
                "\nBrief: {article['description']}" for article in news_articles]

    # sending the message
    client = Client(TWILLO_SID, TWILLO_AUTH_TOKEN)
    for article in articles:
        message = client.messages.create(
            body=article,
            from_='+12567767982',
            to='+919028233983'
        )
        print(message.status)


