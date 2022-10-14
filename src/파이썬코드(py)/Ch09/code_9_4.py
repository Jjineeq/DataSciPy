from wordcloud import WordCloud, STOPWORDS
import wikipedia
import matplotlib.pyplot as plt

wiki = wikipedia.page("Python(programming language)")

#text = wikipedia.page(wiki)
text = wiki.content

wordcloud = WordCloud(width = 2000, height = 1500).generate(text)

plt.figure(figsize= (40,30))
plt.imshow(wordcloud)
plt.show()