# Description

It is time to get our hands dirty and to manipulate some real world data. You have been hired by a new company named EncyclEarthpedia and your first task it build a search engine. EncyclEarthpedia is an online encyclopedia but specialized in the planet Earth, its geology, biology, and everything related to the Earth.

The search engine should be simple at first. The user needs to be able to type some words and the engine returns the most relevant articles.

There is a problem though. The engineers working on the database messed up and EncyclEarthpedia's database and API are not available for a week. This is a bummer ! If we can't have access to the articles, how are we going to build our engine ?

# Task

Instead of waiting for a week, we are going to build a simple model for some similar article from Wikipedia.

What we are going to do is:

Get some article from Wikipedia to work with.
Extract meaningful and usable content from this article.
Clean up and filter the data to narrow the scope to relevant words
Build a simple frequency model.
Analysing the article based on this model.
This first work of this article would be the start of our search engine, using some notion from Information Retrieval and tf-idf statistic.

First things first: Let's get the content of this article into code variables.

→ Use Wikipedia's API to retrieve the content of the article

Create a function get_content(article_name) to retrieve information about an article.

→ Using pip install wikipedia and import wikipedia is strictly forbidden!

Printing your result, you should see something similiar to:

# Installation

# Usage

Run my_mr_clean_ipynb Jupyter File :)