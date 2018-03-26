# coding: utf-8
import pandas as pd
import datetime as dt 
import calendar as cd

filename = "chicago.csv" 

city = pd.read_csv(filename) 
time_period = "none"
city['Start Time'] = pd.to_datetime(city['Start Time']) #converts Start Time to datetime object
city['month'] = city['Start Time'].dt.month #converts month to datetime object
city['weekday'] = city['Start Time'].dt.weekday_name #converts day of week to daytime object
city['hour'] = city['Start Time'].dt.hour

#st1 = city.sort_values('month')
#std2 = st1.loc[st1['month'] == 3]


print(city.style.format("{:.2%}"))






#print(city_file.sort_values(by = 'Birth Year').iloc[0])
#print(city_file['Start Station'].mode().iloc[0])
#print(city_file)
#pd.to_datetime(city_file['Start Time'], format="%Y-%m-%d %H:%M:%S.%f").sort_values()
#city_file['Start Time'] = pd.to_datetime(city_file['Start Time'])
#city_file['month'] = city_file['Start Time'].dt.month
#print(cd.month_name[city_file['month'].mode().iloc[0]])
#best_trip = city_file.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
#print (best_trip.sort_values('count', ascending=False).iloc[0])
#print(city_file)
#print(city_file)
#print(city_file.groupby(['Start Station', 'End Station']).size())
#print (city_file['User Type'].value_counts())
#print (city_file['End Station'].mode())
#print(city_file['Trip Duration'].mean())
#prop_form = city_file.style
#print (prop_form)#city_file['Start Time'] = pd.to_datetime(city_file['Start Time'])
#print(city_file.head)
#print(city_file.tail)
#print(city_file.sort_values(by = 'Birth Year'))
#print("most popular birth year is " + str(city_file['Birth Year'].mode()))
#try sorting popular gender by day
