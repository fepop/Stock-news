STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests


stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":"O3IWQQTTOGHGJ7GZ",

}

news_params = {

    "apikey":"ab933cfb1d114d8696c268a1d40e9965",
    "q":COMPANY_NAME

}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"





news_response = requests.get(url=NEWS_ENDPOINT,params=news_params)
news = news_response.json()




response = requests.get(url=STOCK_ENDPOINT,params=stock_params)
data = response.json()
data2 = data.items()

data_list = data.items()


data1 = data["Time Series (Daily)"]



data_exe = [value for (key,value) in data1.items()]








yesterday = data_exe[0]

close2daysago = data_exe[1]["4. close"]

closeyesterday = data_exe[0]["4. close"]





difference = round(abs(float(closeyesterday) - float(close2daysago)))



diff_percent = difference/float(closeyesterday) * 100

final_percent = round(diff_percent,2)




if 6 > 5:
    three_articles = news["articles"][:3]
    formated_article = [f"headline: {article['title']}. \ndescription:{article['description']}\n" for article in three_articles]

for i in formated_article:
    print(i)

   

