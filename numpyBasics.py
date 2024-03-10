#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


array2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(array2.shape)
a = array2.reshape(3,5)
print(a)


# In[ ]:


print("Shape:",a.shape)
print("Dimentsion:",a.ndim)
print("Data Type:",a.dtype.name)
print("Size",a.size)
printf("Type",type(a))


# In[ ]:


x=np.array([1,2,3])
y=np.array([4,5,6])
print(x+y)
print(x-y)
print(x**2)


# In[ ]:


a=np.array([1,2,3])
d=a.copy()
print(d)
b=a
c=a
b[0]=5
print(a,b,c)


# In[ ]:


a=np.array([1,2,3,4,5,6,7])
print(b)
print(b[1,1])
print(b[:,1])
print(b[1,:])
print(b[1,1:4])
print(b[-1,:])
print(b[:,-1])

