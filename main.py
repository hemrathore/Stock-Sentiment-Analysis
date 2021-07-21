from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer #allows to apply sentiment analysis on any text
import pandas as pd
from pandas.core.frame import DataFrame 
import matplotlib.pyplot as plt

finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AMZN', 'GOOG', 'FB']

news_tables = {} # dictionary
for ticker in tickers:
    url = finviz_url + ticker

    req = Request(url = url, headers={'user-agent': 'my-app'}) #requesting url
    response = urlopen(req) #opening url
    
    html = BeautifulSoup(response, 'html') #html parser (parsing html code from here)
    news_table = html.find(id = 'news-table')
    news_tables[ticker] = news_table # here ticker is key and creating dictionary

    #saving as dictionary then will parse each table individually


parsed_data = []

for ticker, news_table in news_tables.items():         #items() method is used to return the list with all dictionary keys with values.
    for row in news_table.findAll('tr'):
        title = row.a.get_text()                       #The get_text() method returns the text inside the Beautiful Soup or Tag object as a single Unicode string.
        date_data = row.td.text.split(' ')             #here get_text and text is the same

        if len(date_data) == 1:
            time = date_data[0]
        else:
            date = date_data[0]
            time = date_data[1]
        
        parsed_data.append([ticker, date, time, title])

df = pd.DataFrame(parsed_data, columns = ['ticker', 'date', 'time', 'title'])

vader = SentimentIntensityAnalyzer()

f = lambda title: vader.polarity_scores(title)['compound']    #just to get the compound score
df['compound'] = df['title'].apply(f)
df['date'] = pd.to_datetime(df.date).dt.date   #convert date to standard date time format

mean_df = df.groupby(['ticker', 'date']).mean()
mean_df = mean_df.unstack()
mean_df = mean_df.xs('compound', axis="columns").transpose()                #Using the xs() function to get cross-section from the DataFrame. This method takes a key argument to select data at a particular level of a MultiIndex.
mean_df.plot(kind = 'bar')
plt.show()