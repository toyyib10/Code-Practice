#!/usr/bin/env python
# coding: utf-8

# In[40]:


####youtube id finder
inp = input('Enter link: ')
if '=' in inp:
    d = inp.split('=')
elif 'youtu.be' in inp:
    f = inp.split('/')
r = len(f)
print(f[r - 1])


# In[55]:


#secret message
import string
d = ("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,s,y,z")
dd = d.upper()
x = dd.split(',')
print(x)
c = 0
for i in x:
    c += 1 
print(c)

