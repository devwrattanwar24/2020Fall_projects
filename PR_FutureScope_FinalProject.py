#!/usr/bin/env python
# coding: utf-8

# ## This document is a test environment for our final project. If we were to expand this project and incorporate other elements, this would be our starting point. We would like to explore heatmaps, through a geographical lens, with more depth to uncover various trends in arrests/complaints by the hour, day, week, month etc. 
# 
# References: <br> https://towardsdatascience.com/data-101s-spatial-visualizations-and-analysis-in-python-with-folium-39730da2adf </br>
# <br> https://github.com/python-visualization/folium/tree/master/examples </br>
# 
# Datasets:
# NYPD Complaint Data Historic - https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i 
# <br>NYPD Arrest Data Historic - https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc

# In[1]:


# Importing relevant libraries and changing the working directory

import pandas as pd
from folium import Map
from folium.plugins import HeatMap
from folium.plugins import HeatMapWithTime
import os

os.chdir('D:/Downloads/')


# In[2]:


# Reading the dataset into a pandas dataframe

arrests_2019 = pd.read_csv('NYPD_Arrests_Data_2019.csv')


# In[3]:


arrests_2019.head()


# In[4]:


# Choosing relevant columns for analysis

arrests_locations = arrests_2019[['Latitude', 'Longitude']]


# In[5]:


arrests_locations.head()


# In[6]:


# Creating a base map function to facilitate analysis for geographic heatmaps

def generateBaseMap(default_location = [40.693943, -73.985880], default_zoom_start = 11):
    base_map = Map(location = default_location, control_scale = True, zoom_start = default_zoom_start)
    return base_map


# In[7]:


arrests_map = generateBaseMap()
HeatMap(data = arrests_locations[['Latitude', 'Longitude']], radius=8, max_zoom=13).add_to(arrests_map)
arrests_map


# In[8]:


# Reading the complaints data in a pandas dataframe

complaints_2019 = pd.read_csv('NYPD_Complaint_Data_Historic_2019.csv')


# In[9]:


complaints_2019.head()


# In[10]:


# Choosing relevant columns

complaints_locations = complaints_2019[['Latitude', 'Longitude']]


# In[11]:


complaints_locations.head()


# In[12]:


# Creating a heatmap for the complaints data

complaints_map = generateBaseMap()

HeatMap(data=complaints_locations[['Latitude', 'Longitude']], radius = 8, max_zoom = 13).add_to(complaints_map)


# In[13]:


complaints_map


# In[14]:


arrests_map


# ## Interactive Plot - Arrests by Day of the Year (1 - 365) and location

# In[15]:


# Choosing relevant columns to create an interactive plot

arrests_loc_time = arrests_2019[['Latitude', 'Longitude', 'ARREST_DATE']]
arrests_loc_time.head()


# In[16]:


arrests_loc_time['ARREST_DATE'] = pd.to_datetime(arrests_loc_time['ARREST_DATE'], infer_datetime_format=True)
arrests_loc_time.head()


# In[17]:


arrests_loc_time['Day'] = arrests_loc_time.ARREST_DATE.apply(lambda x: x.dayofyear)


# In[18]:


arrests_loc_time.head()


# In[19]:


heatmap = [[[row['Latitude'], row['Longitude']] for index, row in arrests_loc_time[arrests_loc_time['Day'] == i].iterrows()] for i in range(1,365)]


# In[20]:


# Major inspiration taken from -> https://towardsdatascience.com/data-101s-spatial-visualizations-and-analysis-in-python-with-folium-39730da2adf
# Used their code snippet 

base_map_DOY = generateBaseMap(default_zoom_start = 11)
HeatMapWithTime(heatmap, radius = 5, gradient = {0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 1: 'red'}, min_opacity = 0.5, max_opacity = 0.8, use_local_extrema = True).add_to(base_map_DOY)
base_map_DOY


# ## Interactive Plot - Complaints by the hour and location

# In[21]:


complaints_time = complaints_2019[['Latitude', 'Longitude', 'CMPLNT_FR_TM']]


# In[22]:


complaints_time.head()


# In[23]:


complaints_time['CMPLNT_FR_TM'] = pd.to_datetime(complaints_time['CMPLNT_FR_TM'], infer_datetime_format=True)


# In[24]:


complaints_time.head()


# In[25]:


complaints_time['Hour'] = complaints_time.CMPLNT_FR_TM.apply(lambda x: x.hour)


# In[26]:


complaints_time.head()


# In[27]:


heatmap_hour = [[[row['Latitude'], row['Longitude']] for index, row in complaints_time[complaints_time['Hour'] == i].iterrows()] for i in range(0,24)]


# In[28]:


base_map_hour = generateBaseMap(default_zoom_start=11)
HeatMapWithTime(heatmap_hour, radius=5, gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 1: 'red'}, min_opacity=0.5, max_opacity=0.8, use_local_extrema=True).add_to(base_map_hour)
base_map_hour

