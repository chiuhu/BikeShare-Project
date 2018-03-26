# coding: utf-8
## TODO: import all necessary packages and functions
import datetime as dt
import pandas as pd
import calendar as cd
import time
import csv



## Filenames
#chicago = 'chicago.csv'
chicago = pd.read_csv('chicago.csv')
new_york_city = pd.read_csv('new_york_city.csv')
washington = pd.read_csv('washington.csv')


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
                 # TODO: handle raw input and complete function
        if city.lower() in ["chicago", "washington", "new york"]:
            if city == "Chicago":
                city = chicago
            elif city == "Washington":
                city = washington
            else:
                city = new_york_city
            print (city)
            break
        else:
            print(city +" is not a valid choice, please try again.\n "
                "Program restarting ......\n")

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''

    # TODO: handle raw input and complete function
    while True:
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n')
        if time_period.lower() in ["month", "day","none"]:
            if time_period.lower() == "month":
                time_period = ("month")
            elif time_period.lower() == "day":
                time_period = ("day")
            else:
                time_period = ("none")
            print(time_period)
            break
        else:
            print(time_period +" is not a valid choice, please try again.")

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n')
        # TODO: handle raw input and complete function
        if month.lower() in ["january", "february", "march", "april", "june"]:
            if month.lower() == "january":
                month = "january"
            elif month.lower() == "february":
                month = "february"
            elif month.lower() == "march":
                month = "march"
            elif month.lower() == "april":
                month = "april"
            elif month.lower() == "may":
                month = "may"
            else:
                month = "june"
            print(month)
            break
        else:
            print(month +" is not a valid choice, please try again.")
def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    city_file['Start Time'] = pd.to_datetime(city_file['Start Time'])
    city_file['month'] = city_file['Start Time'].dt.month
    print(cd.month_name[city_file['month'].mode().iloc[0]]) #returns most popular month

def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    city_file['Start Time'] = pd.to_datetime(city_file['Start Time'])
    city_file['weekday'] = city_file['Start Time'].dt.weekday_name
    print(city_file['weekday'].mode().iloc[0]) #returns most popular day in list


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    city_file['Start Time'] = pd.to_datetime(city_file['Start Time'])
    city_file['hour'] = city_file['Start Time'].dt.hour
    return city_file['hour'].mode().iloc[0]
    print(city_file['hour'].mode().iloc[0]) #returns most popular hour overall as int

def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: comp+lete function
    av_duration = city_file['Duration'].sum()
    tot_duration = city_file['Duration'].mean()
    print(av_duration)
    print(tot_duration)


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    pop_start_station = city_file['Start Station'].mode()
    pop_end_station = city_file['End Station'].mode()
    print(pop_end_station)
    print(pop_start_station)


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    #print(city_file.groupby(['Start Station', 'End Station']).size()) #returns trip counts fix to find popular trip
    best_trip = city_file.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
    print (best_trip.sort_values('count', ascending=False).iloc[0])

def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    print(city_file['User Type'].value_counts())


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    print(city_file['Gender'].value_counts())


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function
    print("most popular birth year is " + str(city_file['Birth Year'].mode().iloc[0]))
    print(city_file.sort_values(by = 'Birth Year').iloc[0]) #Oldest
    print(city_file.sort_values('Birth Year', ascending=False).iloc[0]) #Youngest

def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city_file = get_city()
    # Filter by time period (month, day, none)
    time_period = get_time_period()

    if time_period == 'month':
        get_month()
    elif time_period == "day":
        get_day()
    else:
        continue

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == "none":
        start_time = time.time()
        popular_month(city_file, time_period)
        #TODO: call popular_month function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == "none" or time_period == "month":
        start_time = time.time()

        # TODO: call popular_day function and print the results
        popular_day(city_file, time_period)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    #popular_hour(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    #trip_duration(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    gender(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    birth_years(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
