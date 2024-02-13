# My_Mr_Clean

## Task

The task is to take the content of this site [URl](https://en.wikipedia.org/wiki/Ozone_layer) and display the top 20 most frequently used words

## Description

This code takes the content of this site using the function `def get_content(name)`, and starts cleaning it from unnecessary characters such as `(r'\[\[.*?\]\]|\{.*?\}|<.*?>', '')` to an empty line
using the `def merge_contents(data)` function. After that, we sort our text `def words_sort(param)`.
Using `def tokenize(param)` function. We once again clear our site of commas and articles from the English language and translate all this into lower letters for counting with the `def lower_collection(param)` function. We translate our text into json format `def count_frequency(collection`) and read the most frequently used words using the `def print_most_frequent(frequencies, n)` function.
And the simplest thing remains, just display it all in a diagram `def matplotlib(cleaned_list, top_n)`.

## Installation

For this program to work correctly you need to install these libraries

``` python
    pip3 install ssl
    pip3 install requests
    pip3 install bs4
    pip3 install matplotlib
    pip3 install numpy
    pip3 install nltk
```
___

## Library info

Computers sometimes ask for SSL access and to avoid this we need an `ssl` library
We need a request to send a `request` to the site
We need `Bs4` to find information
We need `Matplotlib` to output the diagram 
`Numpy` For convenience
`Nltk` for stop words

## Help



If you have any questions, you can contact me by mail

>mirabbosminavarov@gmail.com
