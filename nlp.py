#!/usr/bin/env python
# coding: utf-8

# In[64]:


pip install nltk


# In[8]:


import nltk


# In[10]:


nltk.download('punkt')


# In[24]:


import nltk
from nltk import sent_tokenize,word_tokenize


# In[26]:


sentence="Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).The idea behind inheritance in Java is that you can create new classes that are built upon existing classes. When you inherit from an existing class, you can reuse methods and fields of the parent class.Moreover, you can add new methods and fields in your current class also.Inheritance is a fundamental concept in object-oriented programming (OOP). It allows one class to inherit the properties and behaviors (methods and attributes) of another class. The class that inherits is called a subclass or derived class, while the class being inherited from is called the superclass or base class. Inheritance promotes code reusability and the creation of a hierarchical structure in your code."


# In[27]:


# seperation of sentence
sent_tokenize(sentence)


# In[28]:


# count sentence
len(sent_tokenize(sentence))


# In[29]:


word_tokenize(sentence)


# In[30]:


len(word_tokenize(sentence))


# In[31]:


tokens=word_tokenize(sentence)


# In[32]:


print(tokens)


# In[33]:


for word in tokens:
    for i in range (0,len(word)):
        print(word[i])


# In[42]:


text="To be true or not to be true"


# In[43]:


import nltk


# In[44]:


tokens=nltk.word_tokenize(text)


# In[45]:


print(tokens)


# In[52]:


bi=list(nltk.bigrams(text))


# In[53]:


print(bi)


# In[56]:


tri=list(nltk.trigrams(tokens))


# In[58]:


print(tri)


# In[66]:


ngram=list(nltk.ngrams(tokens,6))


# In[67]:


print(ngram)


# In[ ]:




