#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = "https://www.nytimes.com/2020/12/29/nyregion/nyc-2020-crime-covid.html"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')
tags = soup.find('section', class_ = "meteredContent css-1r7ky0e")
text = tags.get_text()
text2 = text.lower()


# In[4]:


word_dict = {}
for word in text2.split():
    if word not in word_dict:
        word_dict[word] = 0
    word_dict[word] += 1
sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))


# In[5]:


stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
filtered_dict = {}
for key, value in sorted_dict.items():
    if key not in stopwords:
        filtered_dict[key] = value
#print(filtered_dict)


# In[6]:


import pandas as pd
df = pd.DataFrame(list(filtered_dict.items()),columns = ['word','count']) 
df_top30 = df[0:25]


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[8]:


ordered_df = df_top30.sort_values(by='count')
my_range=range(1,len(ordered_df.index)+1)
plt.hlines(y=my_range, xmin=0, xmax=ordered_df['count'], color='green')
plt.plot(ordered_df['count'], my_range, "o")
plt.yticks(my_range, ordered_df['word'])
plt.title("The Top 25 Words Used by the New York Times \nto Describe NYC Crime in 2020", loc='center')
plt.xlabel('Word Count')
plt.ylabel('Word')
plt.show()


# In[16]:


height = list(df_top30["count"])
bars = tuple(df_top30["word"])
x_pos = np.arange(len(bars))
plt.bar(x_pos, height, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
# Create names on the x-axis
plt.xticks(x_pos, bars, rotation=90)
plt.title("The Top 25 Words Used by the New York Times \nto Describe NYC Crime in 2020", loc='center')
plt.ylabel('Word Count')
plt.xlabel('Word')
# Show graph
plt.show()


# In[51]:


url = "https://www.thecity.nyc/2020/12/21/22189682/why-are-shootings-up-in-new-york-city-in-2020-nypd"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')
tags = soup.find('div', class_ = "c-entry-content")
text3 = tags.get_text()
text4 = text.lower()


# In[52]:


word_dict = {}
for word in text4.split():
    if word not in word_dict:
        word_dict[word] = 0
    word_dict[word] += 1
sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))


# In[53]:


stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
filtered_dict = {}
for key, value in sorted_dict.items():
    if key not in stopwords:
        filtered_dict[key] = value
#print(filtered_dict)


# In[54]:


import pandas as pd
df = pd.DataFrame(list(filtered_dict.items()),columns = ['word','count']) 
df_top30 = df[0:25]


# In[55]:


ordered_df = df_top30.sort_values(by='count')
my_range=range(1,len(ordered_df.index)+1)
plt.hlines(y=my_range, xmin=0, xmax=ordered_df['count'], color='green')
plt.plot(ordered_df['count'], my_range, "o")
plt.yticks(my_range, ordered_df['word'])
plt.title("The Top 25 Words Used by the 'The City' \nto Describe NYC Crime in 2020", loc='center')
plt.xlabel('Word Count')
plt.ylabel('Word')
plt.show()


# In[56]:


url = "https://www.nydailynews.com/new-york/nyc-crime/ny-nypd-closes-book-on-2020-20210101-hbaknpnvxfflvj432oum6s3ewe-story.html"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')
tags = soup.find('div', class_ = "wrapper clearfix pb-curated full pb-feature pb-layout-item pb-f-article-body")
text5 = tags.get_text()
text6 = text.lower()


# In[61]:


word_dict = {}
for word in text6.split():
    if word not in word_dict:
        word_dict[word] = 0
    word_dict[word] += 1
sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))


# In[62]:


stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
filtered_dict = {}
for key, value in sorted_dict.items():
    if key not in stopwords:
        filtered_dict[key] = value
#print(filtered_dict)


# In[63]:


import pandas as pd
df = pd.DataFrame(list(filtered_dict.items()),columns = ['word','count']) 
df_top30 = df[0:25]


# In[64]:


names='police/nypd', 'shot/shootings', 'new york city', 'advertisement'
values=[18, 13, 6, 5]
explode = (0.0, 0.05, 0.0, 0)  
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(values, labels=names, labeldistance=1.15, explode = explode, autopct='%1.1f%%',
        shadow=True, startangle=90, colors = colors);
plt.title("Four Common Used Words by NYDailyNews \nto Describe NYC Crime", loc='center')
plt.show()


# In[76]:


all_text = text2 + text4 + text6
all_dict = {}
for word in all_text.split():
    if word not in all_dict:
        all_dict[word] = 0
    all_dict[word] += 1
all_sorted = dict(sorted(all_dict.items(), key=lambda item: item[1], reverse = True))
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
all_filtered = {}
for key, value in all_sorted.items():
    if key not in stopwords:
        all_filtered[key] = value


# In[77]:


import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle


# In[78]:


# creation of a dataframe
data ={'word': ['police/nypd', 'shot/shooting',
                 'new york city', 'cops/officers', 'crime'],
       'count': [45, 39, 18, 26, 9]
     }
  
df = pd.DataFrame(data)
  
# To plot the waffle Chart
fig = plt.figure(
    FigureClass = Waffle,
    rows = 5,
    values = df.count,
    labels = list(df.word)
)


# In[ ]:




