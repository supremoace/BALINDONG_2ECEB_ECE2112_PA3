#!/usr/bin/env python
# coding: utf-8

# PA3.1

# In[2]:


import pandas as pd

cars = pd.read_csv('cars.csv')
cars


# In[3]:


display = pd.concat([cars.iloc[0:5],cars.iloc[27:32]])
print("The first and last 5 cars are:")

display


# In[ ]:


get_ipython().system('jupyter nbconvert --to script "PA3.1.ipynb"')


# In[ ]:




