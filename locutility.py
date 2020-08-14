# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:15:37 2020

@author: CCCam

Function to fetch location data from dataframe containing city and state column. Used in jupyter notebbok.
"""

from geopy.geocoders import Nominatim
import pandas as pd

def getLocations(df):
    geolocator = Nominatim(user_agent='myapplication') #initialize geolocator

    counts=pd.crosstab(columns=df['Public/Private'],index=[df['State'],df['City']]) #dataframe of college counts at each city 

    #lists to store location data
    lons =[] 
    lats =[] 
    nums =[]
    fundings =[]

    for funding in counts:
        for loc, count in zip(counts.index,counts[funding]):
            #skip if no colleges at that location
            if count==0:
                continue
        
            #fetch location
            location = geolocator.geocode(loc[0]+', '+loc[1]+', US')
            
            #skip if location not found
            if location is None or str(location).split(', ')[-1]!='United States of America':
                continue
            
            #store data
            lats.append(location.latitude)
            lons.append(location.longitude)
            nums.append(count)
            fundings.append(funding)
            
    return (lons,lats,nums,fundings)
