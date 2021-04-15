#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


def get_soup(url):
    '''In this function, a user inputs a URL of an article they want scraped and 
        the function uses requests.get, BeautifulSoup and returns so that the use
        can use HTML to parse throught the soup object'''
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    return soup


# In[17]:


def get_filtered_dict(tags):
    '''This function takes in the tags that came from the url and cleans up the tags by
        just getting the text, putting it into a dictionary, removing common words from
        the dictionary and counting how many times it appears'''
    text = tags.get_text().strip()
    text2 = text.lower()
    word_dict = {}
    for word in text2.split():
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))
    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    filtered_dict = {}
    for key, value in sorted_dict.items():
        if key not in stopwords:
            filtered_dict[key] = value
    return filtered_dict


# In[18]:


soup_1 = get_soup("https://www.forbes.com/advisor/investing/weather-effect-stock-market/")
tags1 = soup_1.find('div', class_ = "article-body inarticle-link-tracking fs-article fs-responsive-text current-article")
filtered_dict1 = get_filtered_dict(tags1)


# In[19]:


plt.figure(figsize=(10,10))
filtered_dict1 = get_filtered_dict(tags1)
df1 = pd.DataFrame(list(filtered_dict1.items()),columns = ['word','count']) 
df_top25_1 = df1[0:25]
ordered_df_1 = df_top25_1.sort_values(by='count')
my_range_1=range(1,len(ordered_df_1.index)+1)
plt.hlines(y=my_range_1, xmin=0, xmax=ordered_df_1['count'], color='blue')
plt.plot(ordered_df_1['count'], my_range_1, "o", color = "black")
plt.yticks(my_range_1, ordered_df_1['word'])
plt.title("The Top 25 Words Used by the Forbes to \n Describe Weather and Stocks", loc='center', fontweight='bold')
plt.xlabel('Word Count')
plt.ylabel('Word')
plt.show()


# In[20]:


soup_2 = get_soup("https://www.investopedia.com/articles/markets/111015/does-weather-affect-stock-market.asp")
tags2 = soup_2.find('div', class_ = "comp article-body-content mntl-sc-page mntl-block")
filtered_dict2 = get_filtered_dict(tags2)


# In[24]:


plt.figure(figsize=(10,10))
df_2 = pd.DataFrame(list(filtered_dict2.items()),columns = ['word','count']) 
df_top25_2 = df_2[0:25]
ordered_df_2 = df_top25_2.sort_values(by='count')
bars = tuple(ordered_df_2['word'])
height = list(ordered_df_2['count'])
y_pos = np.arange(len(bars))
plt.barh(y_pos, height, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
plt.yticks(y_pos, bars)
plt.title("The Top 25 Words Used by the 'Investopedia' \nto Describe NYC Crime in 2020", loc='center', fontweight='bold')
plt.ylabel('Word Count')
plt.ylabel('Word')
plt.show()


# In[29]:


soup_3 = get_soup("https://www.marketwatch.com/story/stock-market-weather-report-has-something-for-bulls-and-bears-2016-09-30")
tags3 = soup_3.find('div', class_ = "article__body article-wrap at16-col16 barrons-article-wrap")
filtered_dict3 = get_filtered_dict(tags3)


# In[32]:


df_3 = pd.DataFrame(list(filtered_dict3.items()),columns = ['word','count']) 
df_top25_3 = df_3[0:25]
print(df_top25_3)


# In[36]:


plt.figure(figsize=(10,10))
names='market/stock', 'sunny/sun', 'stock/investment', 'stormy/cloudy'
values=[13, 8, 6, 3]
explode = (0.0, 0.05, 0.0, 0)  
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(values, labels=names, labeldistance=1.15, explode = explode, autopct='%1.1f%%',
        shadow=True, startangle=90, colors = colors);
plt.title("Investors React More to When It's Sunny than Cloudy (According to MarketWatch)", loc='center', fontweight='bold')
plt.show()


# In[37]:


def get_all_text(tags_list):
    all_text = ""
    for tag in tags_list:
        text = tag.get_text()
        text2 = text.lower()
        all_text += text2
    return all_text
url_list = [tags1, tags2, tags3]
all_text = get_all_text(url_list)
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
#print(all_filtered)


# In[40]:


all_df = pd.DataFrame(list(all_filtered.items()),columns = ['word','count']) 
all_top_25 = all_df[0:25]
#print(all_top_25)


# In[46]:


plt.figure(figsize=(10,10))
ax = plt.subplot(111, polar=True)
plt.axis('off')
upperLimit = 40
lowerLimit = 5
max = all_top_25['count'].max()
slope = (max - lowerLimit) / max
heights = slope * all_top_25['count'] + lowerLimit
width = 2*np.pi / len(all_top_25['word'])
indexes = list(range(1, len(all_top_25.index)+1))
angles = [element * width for element in indexes]

plt.title('Most Common Stock Market Weather Words Used in All Three Articles', loc = 'center', fontweight='bold')

bars = ax.bar(
    x=angles, 
    height=heights, 
    width=width, 
    bottom=lowerLimit,
    linewidth=2, 
    edgecolor="white",
    color="#61a4b2",
)

labelPadding = 1

for bar, angle, height, label in zip(bars,angles, heights, all_top_25["word"]):
    rotation = np.rad2deg(angle)
    alignment = ""
    if angle >= np.pi/2 and angle < 3*np.pi/2:
        alignment = "right"
        rotation = rotation + 180
    else: 
        alignment = "left"

    ax.text(
        x=angle, 
        y=lowerLimit + bar.get_height() + labelPadding, 
        s=label, 
        ha=alignment, 
        va='center', 
        rotation=rotation, 
        rotation_mode="anchor") 


# In[ ]:




