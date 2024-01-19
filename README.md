# 02 Data Science My Mr Clean



Introduction

This project explores data cleaning and analysis techniques essential for building search engines. We'll work with data from Wikipedia to create a simple frequency model, filtering relevant terms, and visualizing word distributions.

Getting Started
    1.Clone this repository.
    2.Install required libraries: requests, bs4, and matplotlib.
    3.Open the my_mr_clean.ipynb notebook.
    4.Follow the instructions within the notebook to complete the tasks.
Tasks
  1. Retrieve Wikipedia Data:

    Use the get_content function to fetch article content from Wikipedia's API.
    Avoid using external libraries like wikipedia.

  2.Clean the Data:

    Extract relevant content using merge_contents.
    Remove markups, URLs, and unnecessary elements.
  3.Tokenize the Text:

        Split the text into words using tokenize.
        Convert words to lowercase for consistency.

4.Analyze Word Frequency:

        Count word occurrences with count_frequency.
        Identify the most frequent words using print_most_frequent.

5.Visualize Word Distribution:

        Create a histogram of the most frequent words.

6.Filter Stop Words:

        Remove common, uninformative words (stop words) using remove_stop_words.
        Visualize word frequencies after filtering.

Key Concepts

    Information Retrieval
    Term Frequency (TF)
    Stop Words
    Vectorization
    Stemming (Optional)


Conclusion

This project demonstrates fundamental data cleaning and analysis techniques for search engines. Building upon this foundation, explore more advanced techniques like TF-IDF and stemming to further refine search results.

