
# coding: utf-8

# ## DICTIONARIES
# Unordered mappings for storing objects
# Use a key-value
# use curly braces and colons to signify the keys and their associated values
# #### When List or when dictionary?
# R: Lists: objects retrieved by location. Can be sorted and indexed; Dictionary: Objects retrieved by key. Can't be sorted. Don't retain order and are not a sequence

# In[130]:


dict =  {'key1': 'value1'
         ,'key2': 'value2'}


# In[131]:


dict


# In[132]:


dict['key1']


# In[133]:


prices_lookup = {'apple': 999.99, 'samsung': 888.88, 'huaweii': 333.33}


# In[134]:


prices_lookup['apple']


# In[135]:


test_keys = {'product_a': [0,1,2,3]
            ,'product_b': ['a', 'b', ['c1', ['c2a', 'c2b'], 'c3']]
            ,'product_c': ['none']}


# In[136]:


test_keys['product_b'][1]


# In[137]:


test_keys['product_b'][2][1]


# In[138]:


test_keys['product_b'][2][1][0]


# In[139]:


test_keys['product_c']


# In[140]:


test_keys['product_b'][2][1][::-1]


# In[141]:


a = test_keys['product_b'][2][1][::-1].pop()


# In[142]:


a


# In[143]:


test_keys = {'product_a': [0,1,2,3]
            ,'product_b': ['a', 'b', ['c1', ['c2a', 'c2b'], 'c3']]
            ,'product_c': {'dict_1': ['d1','d2']
                          ,'dict_2': ['none', 1]
                          }
            }


# In[144]:


test_keys['product_c']['dict_1'][1].upper()


# In[145]:


print(f"{test_keys['product_c']['dict_1'][1].upper()} para manter o respeito!")


# In[146]:


print("{a} preste atencao, rapaziada".format(a=test_keys['product_c']['dict_1'][1].upper()))


# In[147]:


print("{} preste atencao, rapaziada".format(test_keys['product_c']['dict_1'][1].upper()))


# ##### Adicionando um elemnto novo

# In[148]:


test_keys['product_new'] = [{'product_new_k1' : 'novo_1' }, [0, 'a', 'b'] ]


# In[149]:


test_keys


# ##### Misturando varios conceitos

# In[150]:


string = "N" + test_keys['product_new'][0]['product_new_k1'][0:-2][::-1].upper()


# In[158]:


print(f"Muito louco. Isso aqui eh {string}")


# In[159]:


test_keys['product_a'] = ['3', 1, 'bruno', 'nome']


# In[160]:


test_keys


# In[161]:


test_keys.keys()


# In[162]:


test_keys.items()


# In[163]:


test_keys[231] = "Test"


# In[164]:


test_keys


# In[165]:


test_keys[231]

