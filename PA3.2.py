#!/usr/bin/env python
# coding: utf-8

# PA3.2

# In[1]:


import pandas as pd

cars = pd.read_csv('cars.csv')
cars


# a. Display First 5 odd number columns

# In[2]:


odd_num_rows = cars.iloc[:,::2]
odd_num_rows


# b. Display the row of the model "Mazda RX4"

# In[3]:


cars.loc[cars['Model'] == 'Mazda RX4']


# c. How many cylinders does Camaro Z28 have?

# In[4]:


cam_cyl = cars.loc[cars['Model']== 'Camaro Z28','cyl'].iloc[0]

print("Cylinders of Camaro Z28: ",cam_cyl)


# d. How many cylinders and what gear type do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have?

# In[5]:


Mazda = cars.loc[cars["Model"]== 'Mazda RX4 Wag', ['Model','cyl', 'gear']] 
Ford = cars.loc[cars["Model"]== 'Ford Pantera L', ['Model','cyl', 'gear']]
Honda = cars.loc[cars["Model"]== 'Honda Civic', ['Model','cyl', 'gear']]

print("The car's gears and cylinders are: ")
pd.concat([Mazda, Ford, Honda])


# In[ ]:


get_ipython().system('jupyter nbconvert --to script "PA3.2.ipynb"')


# In[ ]:




