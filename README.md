# Scrapping WEB site wikipedia

### This code takes the url and parses it into frequently used words and outputs the top 20 words in the form of a diagram

## All the necessary libraries

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