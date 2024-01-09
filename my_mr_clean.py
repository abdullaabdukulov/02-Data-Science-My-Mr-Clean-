import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def get_content(article_name):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": article_name,
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        return data
    else:
        return None

article_name = "Ozone_layer"
data = get_content(article_name)


def merge_contents(html_content):
    page = next(iter(html_content["query"]["pages"].values()))
    page = page["extract"]
    soup = BeautifulSoup(page, 'html.parser')
    div_el = soup.find_all('p')
    data_string =""
    for p in div_el:
        data_string += p.get_text()
    
    return data_string

  # Use the fetched Wikipedia content
merged_data = merge_contents(data)

def tokenize(content):
    content = content.replace(".", " ").replace("("," ").replace("]", " ").replace("[", " ").replace(")", " ")
    content = content.replace("\"", " ").replace("–", " ").replace(",", " ").replace("-", " ").replace(" <", " ").replace(" >", " ").replace(";", " ")
    content = content.replace("  /", " ").replace(" b ", " ").replace("\n", " ")
    content = content.replace("1", " ").replace("2", " ").replace("3", " ").replace("4", " ").replace("5", " ").replace("6", " ").replace("7", " ").replace("8", " ").replace("9", " ").replace("0", " ")
    data_array = content.strip(".").split()
    return data_array
collection = tokenize(merged_data)

def lower_collection(collection):
    
    lower_array = []
    for i in collection:
        lower_array.append(i.lower())
    return lower_array

collection = lower_collection(collection)

def remove_stop_words(words, stop_words):
    return [i for i in words if i not in stop_words]

stop_words = ["on", "this","o","or","an","b", "can", "cfcs", "with", "is", "at", "for", "have", "which", "has", "it", "the", "a", "of", "to", "in", "about", 'and', 'by', 'that', 'as', 'are', 'uv', 'was', 'be', 'nm', 'from']
collection = remove_stop_words(collection, stop_words)

def count_frequency(collection):
    
    unique_array =list(set(collection))
    counts_array = []
    for i in unique_array:
        count = collection.count(i)
        counts_array.append(count)
    result_dict = {}
    for i , key in enumerate(unique_array):
        if key not in result_dict or counts_array[i] > result_dict[key]:
            result_dict[key] = counts_array[i]

    sorted_dict = dict(sorted(result_dict.items(), key=lambda item: item[1]))
    
    return sorted_dict


    


def print_most_frequent(frequencies, n):
    keys = list(frequencies.keys())[n:]
    values = list(frequencies.values())[n:]
    plt.style.use('dark_background')
    plt.figure(figsize=(16, 10))
    plt.title("Most common tokens in the Ozone Layer article", fontsize=24, fontweight='bold', fontstyle='italic')
    plt.xticks(fontsize=14, fontstyle='oblique')
    plt.yticks(fontsize=14, fontstyle='oblique')
    plt.ylabel('Words', fontsize=16, fontstyle='italic')
    plt.xlabel('Count of word', fontsize=16, fontstyle='italic')
    plt.barh(keys,values,color=["#F391D7","#F391D7","#F391D7","#F391D7","#FA76AC","#FA76BE","#FA76DE","#F476FA","#E076FA","#DA76FA","#BE69FA","#A269FA","#458BFD","#33E9FF","#33FFF6","#33FFD4","#B8FF33","#E3FF33","#FFF933","#FFD133","#FFA533","#FF8333","#FF6433","#FF4633","#FF3333"])
    plt.show()
frequencies = count_frequency(collection)
print_most_frequent(frequencies, -25)