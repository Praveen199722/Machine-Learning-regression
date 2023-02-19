#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[2]:


#load the model and rb is used for just read 
loaded_model=pickle.load(open("finalized_model_supportvectormachine.sav","rb"))
#we check it and for prediction we can do it
result=loaded_model.predict([[1234,345,4565,567,789]])


# In[3]:


result


# In[ ]:




