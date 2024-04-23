#!/usr/bin/env python
# coding: utf-8

# In[2]:


import redis


# In[3]:


MEMORYDATABASE = redis.Redis('91.102.161.166')


# In[4]:


MEMORYDATABASE.set('Sevinc', '10-11-1998')


# In[6]:


print(MEMORYDATABASE.get('Sevinc'))


# In[17]:


import networkx as nx


# In[35]:


import matplotlib.pyplot as plt


# In[55]:


BS=nx.Graph()
plt.figure(figsize=(20, 16))


# In[57]:


BS.add_node('Lokbatan')
BS.add_node('BinaTM')
BS.add_node('Salyanski')
BS.add_node('Shikhov')
BS.add_node('Sederek')
BS.add_node('Badamdar')
BS.add_node('Bibiheybet')
BS.add_node('Bayil')
BS.add_node('Azneft')
BS.add_node('Sahil')
BS.add_node('28May')
BS.add_node('Meyveli')
BS.add_node('Yasamal')
BS.add_node('20Yanvar')
BS.add_node('Elmler')
BS.add_node('Nizami')


# In[58]:


BS.add_edge("Lokbatan","BinaTM")
BS.add_edge("Lokbatan","Sederek")
BS.add_edge("BinaTM","Salyanski")
BS.add_edge("BinaTM","Sederek")
BS.add_edge("Salyanski","Shikhov")
BS.add_edge("Shikhov","Bibiheybet")
BS.add_edge("Sederek","Shikhov")
BS.add_edge("Bibiheybet","Bayil")
BS.add_edge("Bayil","Azneft")
BS.add_edge("Azneft","Sahil")
BS.add_edge("Sahil","28May")
BS.add_edge("Sederek","Meyveli")
BS.add_edge("Meyveli","Yasamal")
BS.add_edge("Meyveli","Badamdar")
BS.add_edge("Badamdar","28May")
BS.add_edge("Yasamal","20Yanvar")
BS.add_edge("20Yanvar","Elmler")
BS.add_edge("Elmler","Nizami")
BS.add_edge("Yasamal","Nizami")
BS.add_edge("Nizami","28May")


# In[59]:


pos = nx.spring_layout(BS)
nx.draw_networkx(BS,pos=pos, with_labels=True, node_color="tab:green", node_size=2500, font_color="orange", font_weight="bold")
plt.margins(0.1)
plt.show()


# In[61]:


print( nx.shortest_path( BS, 'BinaTM', 'Badamdar' ) )


# In[ ]:




