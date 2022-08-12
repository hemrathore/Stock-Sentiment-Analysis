Using Finviz.com for stock headlines.
Using beautifulsoup to parse the HTML code and get relevant stuff
Create virtual environment with -> virtualenv env
Activate environment env/Scripts/activate
Create main.py
Need request and beutifulsoup module.
import urlopen, Request i used to open that url and request the data
can view html code by view page source can seee a table holds all data with id = news-table
so will create a dictionary news_tables


Test code for single iteration and understanding:
enumerate function gives index or objectnof any list or list item (Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.)
findall() Return all non-overlapping matches of pattern in string, as a list of strings. The string is scanned left-to-right, and matches are returned in the order found.

amzn_data = news_tables ['AMZN']
amzn_rows = amzn_data.findAll('tr')  

for index, row in enumerate(amzn_rows): 
    title = row.a.text # give text inside a tag
    timestamp = row.td.text
    print(timestamp + " " + title)


Using NLTK module
(compound score ranges from -1 to +1 gives cumulative effect considering postive, negative and neutral part)

pip install nltk
go to python console : import nltk , nltk.download() then download vader_lexicon package either by pop up or by nltk.download('vader_lexicon)

Using pandas, a software library written for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.

using a lambda function (A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.)

Parsed the data got the polarity score and add a column containing the compound score next to the title.

Then using matplotlib to create a plot for analysing the trend.

Ticker symbols are just a shorthand way of describing a company's stock.
