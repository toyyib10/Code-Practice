#!/usr/bin/env python
# coding: utf-8

# In[15]:


string = 'ab  c d e fgh i j kl mnn opqr stuvwxyz'
d = list(string)
f = ''
for i in d:
    if i.isalpha():
        f  += i
print(f)

