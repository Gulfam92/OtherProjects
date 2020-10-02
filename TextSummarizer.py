import bs4 as bs
import nltk
import urllib.request
import heapq
import re


# Scrape the website for which text summarization need to be done (Note: Not all website allows to scrap the data/articles from their website.)
scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')

# Read the scraped data from the website and parse the article paragraphs 
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('para')

article_text = ""

for para in paragraphs:
    article_text += para.text


# Removing Square Brackets and Extra Spaces from the text paragraph
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)


# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)


# Tokenize the article texts using NLTK Tokenize library for further processing
sentence_list = nltk.sent_tokenize(article_text)


