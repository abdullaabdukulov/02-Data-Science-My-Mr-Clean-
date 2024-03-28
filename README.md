# Description

It is time to get our hands dirty and to manipulate some real world data. You have been hired by a new company named EncyclEarthpedia and your first task it build a search engine. EncyclEarthpedia is an online encyclopedia but specialized in the planet Earth, its geology, biology, and everything related to the Earth.

The search engine should be simple at first. The user needs to be able to type some words and the engine returns the most relevant articles.

There is a problem though. The engineers working on the database messed up and EncyclEarthpedia's database and API are not available for a week. This is a bummer ! If we can't have access to the articles, how are we going to build our engine ?

Instead of waiting for a week, we are going to build a simple model for some similar article from Wikipedia.

What we are going to do is:

Get some article from Wikipedia to work with.
Extract meaningful and usable content from this article.
Clean up and filter the data to narrow the scope to relevant words
Build a simple frequency model.
Analysing the article based on this model.
This first work of this article would be the start of our search engine, using some notion from Information Retrieval and tf-idf statistic.


# Task

First things first: Let's get the content of this article into code variables.

→ Use Wikipedia's API to retrieve the content of the article

Create a function get_content(article_name) to retrieve information about an article.

→ Using pip install wikipedia and import wikipedia is strictly forbidden!

Printing your result, you should see something similiar to:

data = get_content("Ozone_layer")
print(data)
{'batchcomplete': True,
'query': {'normalized': [{'fromencoded': False,
'from': 'Ozone_layer',
'to': 'Ozone layer'}],
'pages': [{'pageid': 22834,
'ns': 0,
'title': 'Ozone layer',
'revisions': [{'slots': {'main': {'contentmodel': 'wikitext',
'contentformat': 'text/x-wiki',
'content': '{{pp-semi-indef}}
{{short description|Region of Earths stratosphere that absorbs most of the Suns ultraviolet radiation}}
[[File:Ozone cycle.svg|thumb|upright=1.5|[[Ozone-oxygen cycle]] in the ozone layer.]]


The ozone layer or ozone shield is a region of [[Earth]]s [[stratosphere]] that absorbs most of the [[Sun]]s [[ultraviolet]]  radiation. It contains a high concentration of [[ozone]] (O<sub>3</sub>) in relation to other parts of the atmosphere, although still small in relation to other gases in the stratosphere. The ozone layer contains less than 10 parts per million of ozone, while the average ozone concentration in Earths atmosphere as a whole is about 0.3 parts per million. The ozone layer is mainly found in the lower portion of the stratosphere, from approximately {{convert|15|to|35|km|sp=us}} above Earth, although its thickness varies seasonally and geographically.<ref>{{cite web|url=http://www.ozonelayer.noaa.gov/science/basics.htm|title=Ozone Basics|website=NOAA|date=2008-03-20|access-date=2007-01-29|archive-url=https://web.archive.org/web/20171121051325/http://www.ozonelayer.noaa.gov/science/basics.htm|archive-date=2017-11-21|url-status=dead}}&lt;/ref>


The ozone layer was discovered in 1913 by the French physicists [[Charles Fabry]] and [[Henri Buisson]]. Measurements of the sun showed that the radiation sent out from its surface and reaching the ground on Earth is usually consistent with the spectrum of a [[black body]] with a temperature in the range of 5,500–6,000 K (5,227 to 5,727&nbsp;°C), except that there was no radiation below a wavelength of about 310&nbsp;nm at the ultraviolet end of the spectrum. It was deduced that the missing radiation was being absorbed by something in the atmosphere.

# Install & Usage
pip install requests
pip install bs4
pip install operator
pip install pandas
pip install seaborn
pip install matplotlib

jupyter-notebook --no-browser