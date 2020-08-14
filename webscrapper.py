'''
Webscraper used to collect data from forbes.com, and save it to a csv file to be used in jupyter notebook.
'''

#import necessary packages
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0'}

#url of website to scrape data from
url_base = 'https://www.forbes.com'
url = url_base + '/colleges/harvard-university/?list=top-colleges/#5158d24dfaa4' #first college on the list

data={}
count = 1

while(count<=650):
    
    #load in webpage
    req = Request(url=url,headers=headers)
    client = urlopen(req)
    page= client.read()
    client.close()
    soup = BeautifulSoup(page,'html.parser')
    
    #extract college ranking and college name from header
    header = str(soup.h1).replace('<h1>','').replace('</h1>','')
    header_components = header.split()
    
    #add information to dictionary
    if 'RANK' not in data:
        data['RANK']= [header_components[0]]
        data['NAME']= [ ' '.join(header_components[1:])]
    else:
        data['RANK'].append(header_components[0])
        data['NAME'].append(' '.join(header_components[1:]))
                
    #get row labels and values from the table for the specific college
    types = soup.findAll('div', {'class':'profile-row__type'})
    values = soup.findAll('div', {'class':'profile-row__value'})
    
    #add information to dictionary
    index = 0
    all_types =[]
    for Type in types:
        all_types.append(Type.span.text)
        if Type.span.text=='WEBSITE': #website url is accessed in a different way then than the rest of the rows
            if Type.span.text not in data:
                data[Type.span.text]= [values[index].a.text]
            else:
                data[Type.span.text].append(values[index].a.text)
        else:
            if Type.span.text not in data:
                data[Type.span.text]= [values[index].span.text]
            else:
                data[Type.span.text].append(values[index].span.text)
            
        index+=1
    
    #if information is missing from table, add it as 'N/A' 
    for key in data:
        if key not in all_types and key !='RANK' and key != 'NAME':
            data[key].append('N/A')
    
    print(str(count) + '/650')    
    count+=1
    
    #set url to next college in the list and repeat the process
    if count<=650:
        next_college = soup.findAll('a',{'class':'profile-nav__next'})[0].get('href')
        url = url_base + next_college
    
#save data as csv file
df = pd.DataFrame(data)
keys = list(data.keys())
columns={keys[0]:'Rank',keys[1]:'Name',keys[2]:'City & State',keys[3]:'Public/Private',keys[4]:'Undergraduate Population',
         keys[5]:'Student Population', keys[6]:'Net Price',keys[7]:'Average Grant Aid',keys[8]:'Total Annual Cost',
         keys[9]:'Alumni Salary',keys[10]:'Acceptance Rate', keys[11]:'SAT Composite Range',keys[12]:'ACT Composite Range',
         keys[13]:'Website'}
df.rename(columns=columns,inplace=True)
df.to_csv('ForbesAmericasTopColleges2019.csv')
