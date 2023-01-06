#!/usr/bin/env python
# coding: utf-8

# In[144]:


import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np
import re
get_ipython().run_line_magic('matplotlib', 'inline')
os.getcwd()


# In[145]:


gff_file = '/mnt/HC_Volume_18315164/home-jupyter/jupyter-i-berezin-33/shared/homeworks/python_ds_miniprojects/6_gff/gff.tsv'


# In[146]:


df = pd.read_csv(gff_file, sep='\t')


# In[165]:


df.head()


# In[166]:


#Какое значение атрибута Parent самое частое?
pat = r'Parent=(?P<parent>[\w\.]+)'


# In[168]:


parent = df.attributes.str.extract(pat)
parent.value_counts()


# In[169]:


#Какое самое частое значение в колонке type?
df.type.value_counts()

