#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset =pd.read_csv("C:/Users/anshi/Desktop/datasets/train.csv")
dataset.shape
(500,2)
# dataset.tail()
(dataset.head(20))


# In[4]:


# linear regression
import pandas as pd
from sklearn.model_selection import train_test_split  # Corrected import
from sklearn.metrics import mean_squared_error, r2_score  # Corrected import
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv("C:/Users/anshi/Desktop/datasets/train.csv")
dataset.head()


# In[5]:


x = dataset[['Age']]
y = dataset['DailyRate']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train.shape, x_test.shape, y_train.shape, y_test.shape


# In[ ]:


sns.pairplot(dataset)


# In[6]:


model=LinearRegression()
model.fit(x_train,y_train)


# In[7]:


# titanic dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv("C:/Users/anshi/Desktop/datasets/train_tit.csv")
dataset.shape
(500,2)
dataset.head(20)


# In[4]:


# survived
sns.countplot(x='Survived',data=dataset)


# In[5]:


# gender survival
sns.countplot(x='Survived',hue='Sex',data=dataset)


# In[6]:


# survival on the basis of class
sns.countplot(x='Survived',hue='Pclass',data=dataset)


# In[7]:


# based on age

sns.countplot(x='Survived',hue='Age',data=dataset)


# In[8]:


dataset['Age'].plot.hist()


# In[9]:


dataset.info()


# In[10]:


dataset.isnull()


# In[11]:


dataset.isnull().sum()


# In[12]:


dataset.drop('Cabin',inplace=True,axis=1)


# In[13]:


dataset.head(20)


# In[14]:


dataset.isnull().sum()


# In[15]:


dataset.dropna(inplace=True)


# In[16]:


dataset.isnull().sum()


# In[17]:


dataset.head(20)


# In[18]:


pd.get_dummies(dataset['Age'])


# In[19]:


embark=pd.get_dummies(dataset['Embarked'])
embark


# In[20]:


dataset.drop('Ticket',inplace=True,axis=1)
dataset.head(20)


# In[21]:


Sex=pd.get_dummies(dataset['Sex'])
Sex


# In[22]:


# Sex=pd.get_dummies(dataset['Sex'])
Sex.head(10)


# In[23]:


embark.head(10)


# In[24]:


Name=dataset.drop('Name',inplace=True,axis=1)


# In[25]:


dataset.head(20)


# In[26]:


fare=dataset.drop('Fare',inplace=True,axis=1)


# In[27]:


dataset.head(18)


# In[28]:


pcl=pd.get_dummies(dataset['Pclass'],drop_first=True)


# In[29]:


train=pd.concat([dataset,pcl,Sex,embark],axis=1)


# In[65]:


# train.drop(["Sex","Embarked"],axis=1,inplace=True)


# In[56]:


x=train.drop('Survived',axis=1)
y=train['Survived']


# In[57]:


x.columns = x.columns.astype(str)


# In[58]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=101)


# In[59]:


train.head(20)


# In[1]:


from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression(solver='lbfgs', max_iter=1000)
logmodel.fit(x_train,y_train)


# In[11]:


from sklearn.metrics import classification_report

pred = logmodel.predict(x_test)
print(classification_report(y_test, pred))


# In[ ]:




