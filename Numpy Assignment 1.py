#!/usr/bin/env python
# coding: utf-8

# ### Q1. Use numpy to generate array of 25 random numbers sampled from a standard normal distribution
# 

# In[4]:


import numpy as np
a=np.random.normal(0,1,25)
print("25 random numbers from a standard normal distribution:")
print(a)


# ### Q2. Create a random vector of size 30 and find the mean value.
# 

# In[11]:


import numpy as np
a=np.random.seed(8)
a=np.random.rand(30)
a


# ### Q3. Insert 1 to 100 numbers in a numpy array and reshape it to 10*10 matrix.
# 

# In[25]:


import numpy as np
a = np.arange(1,101)
a.reshape((10,10))


# ### Q4. Create a 10x10 array with random values and find the minimum and maximum values.

# In[49]:


import numpy as np
a=np.random.seed(8)
a = np.random.randint(100,size=(10,10))
print("The array of 10 x 10 matrix is:","\n",a)
print("The minimum value is:", np.min(a))
print("The maximum value is:", np.max(a))


# ### Q5. Find Dot product of two arrays
# 
# f = np.array([1,2])
# 
# g = np.array([4,5])
# 
# 

# In[50]:


f = np.array([1,2])

g = np.array([4,5])
print(f)
print(g)
np.dot(f,g)


# ### 6) Concatenate following arrays along axis=0
# 
# x=np.array([[1,2],
#             [3,4]])
# y=np.array([[5,6]])
# 

# In[54]:


x=np.array([[1,2],
            [3,4]])

y=np.array([[5,6]])

np.concatenate((x,y),axis=0)


# ### 7) How to get the common items between two python NumPy arrays?
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 

# In[55]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)


# ### Q8. Sort the numpy array:
# 
# arr = np.array([10,5,8,4,7,2,3,1])

# In[56]:


arr = np.array([10,5,8,4,7,2,3,1])
np.sort(arr)


# In[ ]:




