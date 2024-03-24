#!/usr/bin/env python
# coding: utf-8

# In[133]:


import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


# In[122]:


import pandas as pd

# Load the CSV file
dataset = pd.read_csv("C:/Users/anshi/Desktop/datasets/Social.csv")

x = dataset.iloc[:,2:3].values
y = dataset.iloc[:,4].values

# Print the data to check
dataset


# In[123]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)


# In[124]:


# feature scalling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.transform(x_test)

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
# Assuming x_train and x_test are initially 1D arrays
x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


# In[138]:


# from sklearn.naive_bayes import GaussianNB
classifier=SVC()
classifier.fit(x_train,y_train)
# from sklearn.svm import SVC


# In[140]:


y_pred = classifier.predict(x_test)
y_pred


# In[141]:


y_test


# In[142]:


from sklearn.metrics import confusion_matr ix
cm = confusion_matrix(y_test, y_pred)
cm


# In[145]:


# Accuracy
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

# Recall
recall = recall_score(y_test, y_pred)

# F1 score
f1 = f1_score(y_test, y_pred)

print('Accuracy:', accuracy*100)
print('Precision:', precision*100)
print('Recall:', recall*100)
print('F1 score:', f1*100)


# In[134]:


# # Visualising the Test set results
# from matplotlib.colors import ListedColormap
# x_set, y_set = x_test, y_test
# X1, X2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
#                      np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
# plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
#              alpha = 0.75, cmap = ListedColormap(('yellow', 'green')))
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
#                 c = ListedColormap(('purple', 'green'))(i), label = j)
# plt.title('Naive Bayes (test set)')
# plt.xlabel('Age')
# plt.ylabel('Estimated Salary')
# plt.legend()
# plt.show()


# In[69]:


# # Visualising the Test set results
# from matplotlib.colors import ListedColormap
# x_set, y_set = x_test, y_test
# X1, X2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
#                      nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
# mtp.contourf(X1, X2, classifier.predict(nm.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
#              alpha = 0.75, cmap = ListedColormap(('yellow', 'green')))
# mtp.xlim(X1.min(), X1.max())
# mtp.ylim(X2.min(), X2.max())
# for i, j in enumerate(nm.unique(y_set)):
#     mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
#                 c = ListedColormap(('purple', 'green'))(i), label = j)
# mtp.title('Naive Bayes (test set)')
# mtp.xlabel('Age')
# mtp.ylabel('Estimated Salary')
# mtp.legend()
# mtp.show()

