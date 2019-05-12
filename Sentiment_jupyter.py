#!/usr/bin/env python
# coding: utf-8

# In[36]:


import tweepy
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from  nltk.stem import WordNetLemmatizer
from  nltk.corpus   import  stopwords
from textblob import TextBlob
import matplotlib.pyplot as plt


# In[37]:


consumer_key=""
consumer_secret=""
access_key=""
access_secret=""


# In[41]:


def get_tweets(topic):
    #authenticating twitter with consumer key and consumer  secret
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    #setting access token
    auth.set_access_token(access_key,access_secret)
    #connecting bssetting access tokenpi
    api=tweepy.API(auth)
    #number_of_tweets=50
    tweets=api.search(q=topic,count=10,lang='en')
    tmp=[]
    polarity=[]
    subjectivity=[]

    tweets_for_csv=[tweet.text for tweet in tweets]
    for j in tweets_for_csv:
        tmp.append(j)
    #print("Extracted tweets:",tmp)
    #print("####################################")
    
    for j in tweets:
        analize=TextBlob(j.text)
        check=analize.sentiment
        #print(check)
        polarity.append(analize.sentiment[0])
        subjectivity.append(analize.sentiment[1])
        #lemmatization
    #print("####################################")
    print(polarity)
    print(subjectivity)
    '''lemma=WordNetLemmatizer()
    for i in range(len(tmp)):
        words=word_tokenize(tmp[i])
        newword=[lemma.lemmatize(word) for word in words]
        tmp[i]=' '.join(newword)
    #print(tmp)
    '''
    plt.bar(polarity,subjectivity,label="Sentiment Analysis")


# In[44]:


if __name__=='__main__':
    data=input("Enter topic: ")
get_tweets(data)


# In[43]:


'''
import sys
topic=sys.argv(1)  then run using python3 tweet.py virat
'''


# In[ ]:





# In[ ]:




