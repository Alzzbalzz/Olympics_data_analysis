#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


athletes=pd.read_csv('C:/Users/Alis25/Desktop/DA_Sample/athlete_events.csv')
regions= pd.read_csv('C:/Users/Alis25/Desktop/DA_Sample/noc_regions.csv')


# In[3]:


athletes.head()


# In[4]:


regions.head()


# In[5]:


athletes_df= athletes.merge(regions,how='left',on ='NOC')
athletes_df.head()


# In[6]:


athletes_df.shape


# In[7]:


athletes_df.rename(columns={'region':'Region','notes':'Notes'}, inplace=True);
athletes_df.head()


# In[8]:


#check null values
nan_values = athletes_df.isna()
nan_columns= nan_values.any()
nan_columns


# In[9]:


athletes_df.isnull().sum()


# In[10]:


#india details
athletes_df.query('Team == "India"').head(5)


# In[11]:


#top countries participating
top_10_countries = athletes_df.Team.value_counts().sort_values(ascending=False).head(10)
top_10_countries


# In[12]:


#plot for top 10 Countries
plt.figure(figsize=(12,6))
#plt.xticks(rotation=20)
plt.title('Overall Participation by Country')
sns.barplot(x=top_10_countries.index, y=top_10_countries,palette='Set2');


# In[13]:


#Age distribution of the Athletes
plt.figure(figsize=(12, 6))
plt.title('Age Distribution of the Athletes')
plt.xlabel('Age')
plt.ylabel('Number of participants')
plt.hist(athletes_df.Age, bins = np.arange(10,80,2), color='Black',edgecolor = 'white');


# In[14]:


#Male and Female participants
gender_counts= athletes_df.Sex.value_counts()
gender_counts


# In[15]:


#plotting male and female pie chart
plt.figure(figsize=(12,6))
plt.title('Gender Distribution')
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=150,shadow=True);


# In[16]:


female_participants=athletes_df[(athletes_df.Sex=='F')&(athletes_df.Season=='Summer')][['Sex','Year']]
female_participants=female_participants.groupby('Year').count().reset_index()
female_participants.tail()


# In[17]:


womenOlympics =athletes_df[(athletes_df.Sex =='F') &(athletes_df.Season=='Summer')]


# In[18]:


sns.set(style="darkgrid")
plt.figure(figsize=(20,10))
sns.countplot(x='Year',data=womenOlympics, palette='Spectral')
plt.title('Women Participants')


# In[19]:


part=womenOlympics.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(20,10))
part.loc[:,'F'].plot()
plt.title('Female athletes over time')


# In[20]:


#gold medal athletes
goldmedals=athletes_df[(athletes_df.Medal =='Gold')] 
goldmedals.head()


# In[21]:


goldmedals['ID'][goldmedals['Age']>60].count()


# In[22]:


sporting_event=goldmedals['Sport'][goldmedals['Age']>60]
sporting_event


# In[28]:


#gold medal for each country
goldmedals.Region.value_counts().reset_index(name='Medal').head(5)


# In[32]:


totalGoldMedals=goldmedals.Region.value_counts().reset_index(name='Medal').head(7)
g=sns.catplot(x='index',y='Medal',data=totalGoldMedals,height=5,kind='bar',palette='rocket')
g.despine(left=True)
g.set_xlabels('Top 5 countries')
g.set_ylabels('Number of medals')
plt.title('Gold medals for country')


# In[33]:


not_null_medals=athletes_df[(athletes_df['Height'].notnull())&(athletes_df['Weight'].notnull())]


# In[34]:


plt.figure(figsize=(12,10))
axis=sns.scatterplot(x='Height',y='Weight',data=not_null_medals,hue='Sex')
plt.title('Height vs Weight of Olympic Medalists')


# In[ ]:




