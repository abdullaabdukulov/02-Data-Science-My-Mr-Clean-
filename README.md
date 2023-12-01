# 02 Data Science My Mr Clean


<p class="text-muted m-b-15">
</p><h1>My Mr Clean</h1>
<p>Remember to git add &amp;&amp; git commit &amp;&amp; git push each exercise!</p>
<p>We will execute your function with our test(s), please DO NOT PROVIDE ANY TEST(S) in your file</p>
<p>For each exercise, you will have to create a folder and in this folder, you will have additional files that contain your work. Folder names are provided at the beginning of each exercise under <code>submit directory</code> and specific file names for each exercise are also provided at the beginning of each exercise under <code>submit file(s)</code>.</p>
<hr>
<table>
<thead>
<tr>
<th>My Mr Clean</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Submit directory</td>
<td>.</td>
</tr>
<tr>
<td>Submit file</td>
<td>my_mr_clean.ipynb</td>
</tr>
</tbody>
</table>
<h2>Introduction</h2>
<p>It is time to get our hands dirty and to manipulate some real world data. You have been hired by a new company named EncyclEarthpedia and your first task it build a search engine.
EncyclEarthpedia is an online encyclopedia but specialized in the planet Earth, its geology, biology, and everything related to the Earth.</p>
<p>The search engine should be simple at first. The user needs to be able to type some words and the engine returns the most relevant articles.</p>
<p>There is a problem though. The engineers working on the database messed up and EncyclEarthpedia's database and API are not available for a week.
This is a bummer ! If we can't have access to the articles, how are we going to build our engine ?</p>
<p>Instead of waiting for a week, we are going to build a simple model for some similar article from Wikipedia.</p>
<p>What we are going to do is:</p>
<ol>
<li>Get some article from Wikipedia to work with.</li>
<li>Extract meaningful and usable content from this article.</li>
<li>Clean up and filter the data to narrow the scope to relevant words</li>
<li>Build a simple frequency model.</li>
<li>Analysing the article based on this model.</li>
</ol>
<p>This first work of this article would be the start of our search engine, using some notion from <a href="https://en.wikipedia.org/wiki/Information_retrieval" target="_blank">Information Retrieval</a> and <a href="https://en.wikipedia.org/wiki/Tf-idf" target="_blank">tf-idf statistic</a>.</p>
<h3>Getting the data</h3>
<p>We are going to work with an article about the <a href="https://en.wikipedia.org/wiki/Ozone_layer" target="_blank">Ozone Layer</a>.</p>
<p><img src="https://www.thegef.org/sites/default/files/Ozone_870.jpg" width="500"></p>
<p>First things first: Let's get the content of this article into code variables.</p>
<p>→ <strong>Use Wikipedia's API to retrieve the content of the article</strong></p>
<p>Create a function <code>get_content(article_name)</code> to retrieve information about an article.</p>
<p>→ Using <em>pip install wikipedia</em> and <em>import wikipedia</em> is <strong>strictly forbidden</strong>!</p>
<p>Printing your result, you should see something similiar to:</p>
<pre class=" language-plain"><code class=" language-plain">data = get_content("Ozone_layer")
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

The ozone layer or ozone shield is a region of [[Earth]]s [[stratosphere]] that absorbs most of the [[Sun]]s [[ultraviolet]]  radiation. It contains a high concentration of [[ozone]] (O&lt;sub&gt;3&lt;/sub&gt;) in relation to other parts of the atmosphere, although still small in relation to other gases in the stratosphere. The ozone layer contains less than 10 parts per million of ozone, while the average ozone concentration in Earths atmosphere as a whole is about 0.3 parts per million. The ozone layer is mainly found in the lower portion of the stratosphere, from approximately {{convert|15|to|35|km|sp=us}} above Earth, although its thickness varies seasonally and geographically.&lt;ref&gt;{{cite web|url=http://www.ozonelayer.noaa.gov/science/basics.htm|title=Ozone Basics|website=NOAA|date=2008-03-20|access-date=2007-01-29|archive-url=https://web.archive.org/web/20171121051325/http://www.ozonelayer.noaa.gov/science/basics.htm|archive-date=2017-11-21|url-status=dead}}&lt;/ref&gt;

The ozone layer was discovered in 1913 by the French physicists [[Charles Fabry]] and [[Henri Buisson]]. Measurements of the sun showed that the radiation sent out from its surface and reaching the ground on Earth is usually consistent with the spectrum of a [[black body]] with a temperature in the range of 5,500–6,000 K (5,227 to 5,727&amp;nbsp;°C), except that there was no radiation below a wavelength of about 310&amp;nbsp;nm at the ultraviolet end of the spectrum. It was deduced that the missing radiation was being absorbed by something in the atmosphere.
</code></pre>
<h3>Cleaning</h3>
<p>As you may have notice, the answer from the API is not very user-friendly. It is a big json objects with many keys and values that are not really relevant for us.
What we really want to work with is the actual 'content' of the article. But what do we mean by "content" ? Are the titles or the table of contents useful? (yes). Are the hidden URL relevant to us?</p>
<p>Only the actual content interests us so we need somehow to remove all the flourish like markups, the urls, and any useless words or characters.</p>
<p>→ <strong>First merge and store all the meaningful contents from the big json into a handy variable. Any kind of data structure can be used. A simple list would do the trick though</strong></p>
<pre class=" language-plain"><code class=" language-plain">def merge_contents(data):
	...

merge_content = merge_contents(data)

</code></pre>
<h3>Tokenization</h3>
<p>Now that we retrieve all the contents in one place, it is time to dissect our data and build a list of all the words.</p>
<p>Usually a word is delimited by a space or a new line. With this rule, "Ozone-oxygen" is a word. But it means that "Ozone", "Oxygen", and "Ozone-oxygen" are three different words.
Yet, if the end user type "Ozone" or "Ozone-oxygen" in the search bar, the same results should appear for both searchs! Personally, I think "Ozone-oxygen" should be broken into two words. But you might have another opinion!</p>
<p>→ <strong>Create a list of the "splitter" char. For example, if you think words should be delimited by spaces and new lines, your list is [" ", "\n"].</strong></p>
<p>Now that you defined the words delimiters, let's tokenize our content.</p>
<p>→ <strong>Traverse your brand new data structure and tokenize the words: Create a list of all the words.</strong></p>
<pre class=" language-plain"><code class=" language-plain">def tokenize(content):
	...


collection = tokenize(merge_content)
</code></pre>
<p>Because we do not make any difference between Ozone or ozone or OZONE, a good idea is to have all words in lower case.</p>
<p>→ <strong>Update the collection of words for them to be only lower case</strong>.</p>
<pre class=" language-plain"><code class=" language-plain">def lower_collection(collection):
	...

lower_collection(collection)

</code></pre>
<h3>Term Frequency</h3>
<p>From here, let's step back a little bit and recall what is our objectives. A search engine should find relevant articles based on words in a search bar. In this project we will build a simple frequency model.
In other words, given a word, we need to find the articles in which this word is the most frequent. Let's build a frequency model.</p>
<p>→ <strong>Write a function to count the number of occurrences of each word in the collection.</strong></p>
<p>→ <strong>What are the most frequent words? Write a function to print the n most frequent words along with their frenquency.</strong></p>
<pre class=" language-plain"><code class=" language-plain">def count_frequency(collection):
	...

def print_most_frequent(frequencies, n):
	...

frequencies = count_frequency(collection)

print_most_frequent(frequencies, 10)

</code></pre>
<h3>Visualizing</h3>
<p>Printing the most frequent words is a good way to get a feel of the words distribution, but is not very telling.</p>
<p>→ <strong>Visualize the 20 most frequent words by plotting them in a histogram.</strong></p>
<p>Here is the visualization of the most frequent words from the introduction of the article:</p>
<img src="https://storage.googleapis.com/qwasar-public/track-ds/token_visualization.png" width="700">
<h3>Filtering</h3>
<p>But all the words are not equal. Some words have less importance than others. As we can see on the graph, determiners and articles do not really help understanding the topic of an article or a corpus.
In the 10 most frequent words from the introduction, we see that only 2 of them are really useful to classify the article: "ozone" and "layer".</p>
<p>These "unsignificant" little words are called <a href="https://en.wikipedia.org/wiki/Stop_words" target="_blank">stop words</a>.</p>
<p>→ <strong>Create a list of stop words to remove from the list of words.</strong></p>
<pre class=" language-plain"><code class=" language-plain">stop_words = [ "the", "a", "of", "to", "in", "about" ... ]
</code></pre>
<p>→ <strong>Write a function 'remove_stop_words' that takes as parameters a list of tokens, removes the empty words provided this list and returns the new list resulting from this filtering.</strong></p>
<pre class=" language-plain"><code class=" language-plain">def remove_stop_words(words, stop_words):
	...

filtered_collection = remove_stop_words(collection, stop_words)

</code></pre>
<p>→ <strong>Visualize now in a historgram the 25 most frequent words in the filtered collection.</strong></p>
<p>The most frequent words should be more relevant to match this Ozone layer article content. If the user's search is made of the words "Ozone" and "gas", we can <strong>vectorize</strong> articles and represent them with a vector of size 2. The coefficient of the vectorized article would be the frequencies of the words from the search. By vectorizing all articles this way, we can build some kind of distance between articles.
Another data engineering technique we could have had explored is <a href="https://en.wikipedia.org/wiki/Stemming" target="_blank">stemming</a> to get even more insight about the article.</p>
<p>Here ends our little journey into data exploration and information retrieval. If the database engineers of our team are ready, we can use some of the techniques we have seen to build up a small proff of concept!</p>

<p></p>
