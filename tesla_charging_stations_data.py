# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 01:40:19 2023

@author: Dan
"""

#############   imports
import seaborn as sb
import pandas as pd

tesla_df = pd.read_csv('C:\\Users\Dan\Desktop\Python Files\Csv files\Supercharge Locations.csv',encoding='latin1') 

##########################################################


#each amount of tesla charging stations per country
unique_country_count = tesla_df['Country'].value_counts()

#Turning Series into data frame
country_data = unique_country_count.to_frame()

#Makeing Index a column
country_data.reset_index(inplace=True)

#renaming columns
country_data = country_data.rename(columns={'index':'Country','Country':'Charging Stations'})



#############    each amount of charging sations per state (US)   ############
state_data = tesla_df[tesla_df['Country'] == 'USA'].groupby('State').size()        


#turning series into a data frame
state_stations= state_data.to_frame()

#making index into a column
state_stations.reset_index(inplace=True)

#renaming columns
state_stations.columns = ['State', 'Charging Stations']




#########         by year of release           ########################
yeardata =pd.DataFrame()
tesla_df['Year'] = pd.to_datetime(tesla_df['Open Date']).dt.year

#replace missing values
tesla_df['Open Date'] = tesla_df['Open Date'].fillna('Unknown')

#create num of stations per year (adding columns)
yeardata['Year Count'] = tesla_df['Year'].value_counts()

#turning idex (years) into colunn
yeardata.reset_index(inplace=True)

#renaming (index column)
yeardata = yeardata.rename(columns={'index':'Year'})



#################     Bar graph          #################

#year growth
sb.barplot(x=yeardata['Year'],y = yeardata['Year Count'],data=yeardata)

#state counter
sb.barplot(x=state_stations['State'],y=state_stations['Charging Stations'],data=state_stations)

#unique country graph
sb.barplot(x=country_data['Country'],y=country_data['Charging Stations'],data=country_data)



#converting dataframe to .json
state_stations.to_csv('Charging Stations In USA.csv')
country_data.to_csv('Charging Stations Around The World.csv')
yeardata.to_csv('Stations Built Year By Year.csv')








