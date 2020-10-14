import bs4 as bs
import nltk
import urllib.request
import heapq
import re
import math


# Scrape the website for which text summarization need to be done (Note: Not all website allows to scrap the data/articles from their website.)
scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Java_(programming_language)')

# Read the scraped data from the website and parse the article paragraphs 
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

# Create article texts from the paragraph after parsing the scraped data
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

# Create a list of english stopwords from NLTK corpus to compare and discard these stopwords from the article
stopwords = nltk.corpus.stopwords.words('english')

# create a empty dictionary to store the terms and its frequencies (i.e., number of times) appeared in the article
word_frequencies = {}

# calculate the number of each term appearing in the entire article 
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
#print("Word_Frequencies\n", word_frequencies)
            
total_frequency_count = max(word_frequencies.values())
#print(total_frequency_count)

# calculate the TF(term frequency) of the words in the article
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/total_frequency_count)
    
sentence_scores = {}

# Scoring the sentences based on occurances and availability in the word frequencies list
for sentence in sentence_list:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word_frequencies.keys():
            if len(sentence.split(' ')) < 30:
                if sentence in sentence_scores.keys():
                    sentence_scores[sentence] += word_frequencies[word]
                else:
                    sentence_scores[sentence] = word_frequencies[word]
 
# return total number of sentences in summary based on largest sentence_scores                 
sentences_summary = heapq.nlargest(10, sentence_scores, key = sentence_scores.get)

# join the most scored return sentences to generate final summary of the article/paragraph
summary = ' '.join(sentences_summary)
print("#### Summary of the Article ####\n",)
print()
print(summary)


