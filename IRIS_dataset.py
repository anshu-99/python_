#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Iris Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
dataset=pd.read_csv("C:/Users/anshi/Desktop/datasets/Iris.csv")
dataset.tail(10)


# In[40]:


# dataset.drop('Id',inplace=True,axis=1)
# dataset.head(20)


# In[3]:


dataset.describe()


# In[4]:


dataset.isnull().sum()


# In[5]:


species = np.unique(dataset.loc[:,'Species'])


# In[6]:


dataset['Species'].value_counts()


# In[9]:


tmp=dataset.drop("Id",axis=1)
g=sns.pairplot(tmp,hue='Species',markers='*')
plt.show()


# In[2]:


g = sns.violinplot(y='Species', x='SepalLengthCm', data=dataset, inner='quartile')
plt.show()

g = sns.violinplot(y='Species', x='SepalWidthCm', data=dataset, inner='quartile')
plt.show()

g = sns.violinplot(y='Species', x='PetalLengthCm', data=dataset, inner='quartile')
plt.show()

g = sns.violinplot(y='Species', x='PetalWidthCm', data=dataset, inner='quartile')
plt.show()

