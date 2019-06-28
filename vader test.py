
# coding: utf-8

# In[1]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[2]:


analyser=SentimentIntensityAnalyzer()


# In[3]:


def sentiment_analyzer_scores(sentence):
    score=analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))


# In[4]:


sentiment_analyzer_scores("The phone is super cool.")


# In[15]:


#baseline sentence
sentiment_analyzer_scores("The food is good, but the service is really bad")


# In[6]:


#Punctuation
print(sentiment_analyzer_scores("The food here is good!"))
print(sentiment_analyzer_scores("The food here is good!!"))
print(sentiment_analyzer_scores("The food here is good!!!"))

