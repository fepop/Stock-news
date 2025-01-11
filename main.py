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




    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=STOCK_ENDPOINT,params=stock_params)
data = response.json()
data2 = data.items()

data_list = data.items()


data1 = data["Time Series (Daily)"]


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
data_exe = [value for (key,value) in data1.items()]








yesterday = data_exe[0]
#TODO 2. - Get the day before yesterday's closing stock price
close2daysago = data_exe[1]["4. close"]

closeyesterday = data_exe[0]["4. close"]




#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = round(abs(float(closeyesterday) - float(close2daysago)))



#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = difference/float(closeyesterday) * 100

final_percent = round(diff_percent,2)



#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").")
if 6 > 5:
    three_articles = news["articles"][:3]
    formated_article = [f"headline: {article['title']}. \ndescription:{article['description']}\n" for article in three_articles]

for i in formated_article:
    print(i)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

