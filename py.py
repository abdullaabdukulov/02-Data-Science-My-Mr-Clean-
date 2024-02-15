import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import collections
import numpy as np
import nltk
from nltk.corpus import stopwords

try:
    nltk.data.find('corpora/stopwords.zip')
except LookupError:
    nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

print("You can write name of site like is 'Ozone_layer'")
user = input("Write your site: ")
url = f"https://en.wikipedia.org/wiki/{user}"

def get_content(article_url):
    request = requests.get(article_url)
    soup = BeautifulSoup(request.text, "html.parser")
    content_div = soup.find("div", class_="mw-content-ltr mw-parser-output", dir="ltr")
    cleaned_text = content_div.get_text(strip=True, separator=' ')
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

content = get_content(url)

def merge_contents(data):
    cleaned_content = re.sub(r'\[\[.*?\]\]|\{.*?\}|<.*?>', '', data)
    return cleaned_content

merge_content = merge_contents(content)

def tokenize(param):
    cleaned_list = re.findall(r'\b\w+\b', param.lower())
    cleaned_list = [word for word in cleaned_list if word.lower() not in stop_words and word.lower() not in ["nm", "bm", "doi",
                                                                                                             "uv", "may", "cfcs",
                                                                                                             "pmid", "also", '10',
                                                                                                             '3', '9', '2', 'c', 'b',
                                                                                                             '5', '2011', '1', 'epa', '100']]
    return cleaned_list

tokens = tokenize(merge_content)

def lower_collection(param):
    text = ''.join(param)
    lowercased_text = text.lower()
    cleaned_list = lowercased_text.split()
    return cleaned_list

lower = lower_collection(tokens)

def count_frequency(collection):
    frequencies = {}
    for word in collection:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

count = count_frequency(lower)

def plot_most_frequent(tokens, top_n):
    top = collections.Counter(tokens)
    sorted_word = sorted(top.items(), key=lambda x: x[1], reverse=True)[:top_n][::-1]
    words, frequencies = zip(*sorted_word)
    colors = plt.cm.rainbow(np.linspace(0, 1, len(words)))

    plt.barh(words, frequencies, color=colors)
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title('Word Frequency Chart')
    plt.show()

plot_most_frequent(tokens, 20)