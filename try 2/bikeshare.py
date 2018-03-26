## TODO: import all necessary packages and functions
import pandas as pd
import calendar as cd
import datetime as dt
import time

## Import filenames using pandas and name them accordingly
chicago = pd.read_csv('chicago.csv')
chicago.name = "Chicago"
new_york_city = pd.read_csv('new_york_city.csv')
new_york_city.name = "New York"
washington = pd.read_csv('washington.csv')
washington.name = "Washington"


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) Dataframe for a city's bikeshare data.
    '''
    # TODO: handle raw input and complete function
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
                 # TODO: handle raw input and complete function
        if city.lower() in ["chicago", "washington", "new york"]:
            if city == "chicago":
                city = chicago
            elif city == "washington":
                city = washington
            else:
                city = new_york_city
            return city
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
        (str) Time period selection (e.g day, month or none ) as a string
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
            #print(time_period)
            return time_period
            break
        else:
            print(time_period +" is not a valid choice, please try again.")

def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        (int) Returns selection of month as an integer
    '''
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n')
        # TODO: handle raw input and complete function
        if month.lower() in ["january", "february", "march", "april", "may", "june"]:
            if month.lower() == "january":
                month = 1
            elif month.lower() == "february":
                month = 2
            elif month.lower() == "march":
                month = 3
            elif month.lower() == "april":
                month = 4
            elif month.lower() == "may":
                month = 5
            else:
                month = 6
            return month
            break
        else:
            print(month + " is not a valid choice, please try.")
def get_day():
    '''Asks the user for a day and returns the specified day.
    Args:
        none.
    Returns:
        (str) Day of week as a string
    '''
    # TODO: handle raw input and complete function
    while True:
        day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n')
        if day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday","saturday","sunday"]:
            day = day.lower()
            return day
            break
        else:
            print(month + " is not a valid choice, please try again.")


def popular_month(city, time_period):
    '''
    Called from statistics() to print out popular_month based on user input and city dataframe
    Args:
        city dataframe and time_period
    Returns:
        (str) Prints out most popular month for start time

    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    print(" The most popular month for start time in bikeshare usage is: \n" +"     "+ str(cd.month_name[city['month'].mode().iloc[0]]))

def popular_day(city, time_period):
    '''
    Called from statistics() to print out popular day based on user input and city dataframe
    Args:
        city dataframe and time_period
    Returns:
        (str) Prints out most popular month in terms of start time
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    print(" The most popular day for start time in bikeshare usage is: \n" +"     "+ str(city['weekday'].mode().iloc[0]))

def popular_hour(city, time_period):
    '''
    Called from statistics() to print out popular hour based on user input and city dataframe
    Args:
        city dataframe and time_period
    Returns:
        (str) Prints out most popular hour of day for start time
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    if time_period == "month":
        st1 = city.sort_values('month')
        std2 = st1.loc[st1['month'] == month]
        print (" The most popular hour for start time is: \n" + "     "+ str(std2['hour'].mode().iloc[0]) + ":00 Hrs")
    elif time_period == "day":
        st1 = city.sort_values('weekday')
        std2 = st1.loc[st1['weekday'] == day.title()]
        print (" The most popular hour for start time is: \n" + "     " + str(std2['hour'].mode().iloc[0]) + ":00 Hrs")
    else:
        print(" The most popular hour for start time is: \n"+ "     " + str(city['hour'].mode().iloc[0])+ ":00 Hrs")

def trip_duration(city, time_period):
    '''
    Called from statistics() to print out trip duration based on user input and city dataframe
    Args:
        city dataframe and time_period
    Returns:
        (str) Prints out total trip duration and average trip duration for start time
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    if time_period == "month":
        st1 = city.sort_values('month')
        std2 = st1.loc[st1['month'] == month]
        print (" The total trip duration in seconds is \n" + "     "+ str(std2['Trip Duration'].sum()))
        print (" The average trip duration in seconds is \n" + "     "+ str(std2['Trip Duration'].mean()))
    elif time_period == "day":
        st1 = city.sort_values('weekday')
        std2 = st1.loc[st1['weekday'] == day.title()]
        print (" The total trip duration in seconds is \n" + "     " + str(std2['Trip Duration'].sum()))
        print (" The average trip duration in seconds is \n" + "     " + str(std2['Trip Duration'].mean()))
    else:
        print(" The total trip duration in seconds is: \n" + "     " + str(city['Trip Duration'].sum()))
        print(" The average trip duration in seconds is: \n" + "     " + str(city['Trip Duration'].mean()))
def popular_stations(city, time_period):
    '''
    Called from statistics() to print out popular stations during the month or day
    Args:
        city dataframe and time_period
    Returns:
        (str) Prints out popular end and start stations for start time
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    if time_period == "month":
        st1 = city.sort_values('month')
        std2 = st1.loc[st1['month'] == month]
        print(" The most popular start station in terms of start time is: \n" +"     " + str(std2['Start Station'].mode().iloc[0]))
        print(" The most popular end station in terms of start time is: \n" +"     " + str(std2['End Station'].mode().iloc[0]))
    elif time_period == "day":
        st1 = city.sort_values('weekday')
        std2 = st1.loc[st1['weekday'] == day.title()]
        print(" The most popular start station in terms of start time is: \n" +"     " + str(std2['Start Station'].mode().iloc[0]))
        print(" The most popular end station in terms of end time is: \n" +"     " + str(std2['End Station'].mode().iloc[0]))
    else:
        print (" The most popular start station in terms of start time is: \n" +"     "+ str(city['Start Station'].mode().iloc[0]))
        print (" The most popular start station in terms of end time is: \n" +"     "+ str(city['End Station'].mode().iloc[0]))

def popular_trip(city, time_period):
    '''
    Called from statistics() to print out popular trip for start time
    Args:
        city dataframe and time_period
    Returns:
        (str) Prints out total trip duration and average trip duration for start time
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    if time_period == "month":
        st1 = city.sort_values('month')
        std2 = st1.loc[st1['month'] == month]
        best_trip = std2.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
        std3 = best_trip.sort_values('count', ascending=False).iloc[0]
        print (" The most popular trip by start time is: \n" + "     " + std3.to_string())
    elif time_period == "day":
        st1 = city.sort_values('weekday')
        std2 = st1.loc[st1['weekday'] == day.title()]
        best_trip = std2.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
        std3 = best_trip.sort_values('count', ascending=False).iloc[0]
        print (" The most popular trip by start time is: \n" + "     " + std3.to_string())
    else:
        best_trip = city.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
        std3 = best_trip.sort_values('count', ascending=False).iloc[0]
        print (" The most popular trip by start time is: \n" +"     " + std3.to_string())

def users(city, time_period):
    '''
    Called from statistics() to print out user type for either month or day
    Args:
        city dataframe and time_period
    Returns:
        (str) Prints out user type for start time
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    if time_period == "month":
        st1 = city.sort_values('month')
        std2 = st1.loc[st1['month'] == month]
        std3 = std2['User Type'].value_counts()
        print(" The user count for your selection is \n" + "     " + std3.to_string(header=None))
    elif time_period == "day":
        st1 = city.sort_values('weekday')
        std2 = st1.loc[st1['weekday'] == day.title()]
        std3 = std2['User Type'].value_counts()
        print(" The user count for your selection is \n" + "     " + std3.to_string(header=None))
    else:
        std = city['User Type'].value_counts()
        print(" The user count for your selection is \n" + "     " + std.to_string(header=None))

def gender(city, time_period):
    '''
    Called from statistics() to print out gender counts for dataframe
    Args:
        city dataframe and time_period
    Returns:
        (str) Prints out gender counts for start time
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    if time_period == "month":
        st1 = city.sort_values('month')
        std2 = st1.loc[st1['month'] == month]
        std3 = std2['Gender'].value_counts()
        print(" The gender distribution is \n" +"     "+ std3.to_string(header = None))
    elif time_period == "day":
        st1 = city.sort_values('weekday')
        std2 = st1.loc[st1['weekday'] == day.title()]
        std3 = std2['Gender'].value_counts()
        print(" The gender distribution is \n" +"     "+ std3.to_string(header = None))
    else:
        std = city['Gender'].value_counts()
        print(" The gender distribution is \n" + "     " + std.to_string(header = None))
def birth_years(city, time_period):
    '''
    Called from statistics() to print out oldest, youngest and popular birth years
    Args:
        city dataframe and time_period
    Returns:
        (str) Prints out print out oldest, youngest and popular birth year
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    if time_period == "month":
        st1 = city.sort_values('month')
        std2 = st1.loc[st1['month'] == month]
        print (" The most popular birth year is \n"  +"     "+ str(std2['Birth Year'].mode().iloc[0]))
        print (" The oldest birth year is \n" +"     "+ str(std2.sort_values(by = 'Birth Year').iloc[0,8])) #Oldest
        print (" The most recent birth year is \n"+"     "+ str(std2.sort_values('Birth Year', ascending=False).iloc[0,8]))
    elif time_period == "day":
        st1 = city.sort_values('weekday')
        std2 = st1.loc[st1['weekday'] == day.title()]
        print (" The most popular birth year is \n"  +"     "+ str(std2['Birth Year'].mode().iloc[0]))
        print (" The oldest birth year is is \n" +"     "+ str(std2.sort_values(by = 'Birth Year').iloc[0,8])) #Oldest
        print (" The most recent birth year is \n"+"     "+ str(std2.sort_values('Birth Year', ascending=False).iloc[0,8]))
    else:
        print (" The most popular birth year is \n"  +"     "+ str(city['Birth Year'].mode().iloc[0]))
        print (" The oldest birth year is \n" +"     "+ str(city.sort_values(by = 'Birth Year').iloc[0,8])) #Oldest
        print (" The most recent birth year is \n"+"     "+ str(city.sort_values('Birth Year', ascending=False).iloc[0,8])) #Newest
def display_data(city):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        slice of the dataframe showing five individual trip data points
    '''
    i = 0
    while i < city.size:
        display = input('\nWould you like to view individual trip data?'
                'Type \'yes\' or \'no\'.\n')
        if display.lower() == "yes":
             print(city[i:i+5])
             i += 5
        elif display.lower() == "no":
            break
        else:
            print("Please make a proper selection")

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    # Filter by time period (month, day, none)
    time_period = get_time_period()
    city['Start Time'] = pd.to_datetime(city['Start Time']) #converts Start Time to datetime object
    city['month'] = city['Start Time'].dt.month #converts month to datetime object
    city['weekday'] = city['Start Time'].dt.weekday_name #converts day of week to daytime object
    city['hour'] = city['Start Time'].dt.hour #converts hour of week to daytime object

    if time_period == "month":
        global month
        month = get_month()
    elif time_period == "day":
        global day
        day = get_day()
    else:
        time_period == "none"
    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        popular_month(city, time_period)
        print("     That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        popular_day(city, time_period)
        print("     That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()
    # What is the most popular hour of day for start time?
    popular_hour(city, time_period)
    print("     That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    start_time = time.time()
    # What is the total trip duration and average trip duration?
    trip_duration(city, time_period)
    print("     That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    start_time = time.time()
    # What is the most popular start station and most popular end station?
    popular_stations(city, trip_duration)
    print("     That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    start_time = time.time()
    # What is the most popular trip?
    popular_trip(city, time_period)
    print("     That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    start_time = time.time()
    # What are the counts of each user type?
    users(city, time_period)
    print("     That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    start_time = time.time()
    # What are the counts of gender?
    #if city is not washington since washington lacks the gender column
    if city.name is not "Washington":
        gender(city, time_period)
        print("     That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()
    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    #if city is not washington since washington lacks the birth years column
    if city.name is not "Washington":
        birth_years(city, time_period)
        print("     That took %s seconds." % (time.time() - start_time))


    # Display five lines of data at a time if user specifies that they would like to
    display_data(city)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
