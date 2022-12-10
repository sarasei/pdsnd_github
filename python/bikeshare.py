import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input('\nWhich city do you want to explore? Chicago ,New York City or Washington?\n').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Ooops! it is not a valid city, please enter either .chicago, new york city, or washington')
        
 
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input('\nWhat month do you want to look into? "all" for all months or January, February, March, April, May or June?\n').lower()
      if month not in ('All', 'january', 'february', 'March', 'April', 'May', 'june'):
        print("Sorry! Don't have what you searched for")
        continue
      else:
        break    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nlooking for a specific day? If so, enter: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday. if not, enter: all.\n").lower().title()
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break
              
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
                       
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('\nMost Popular Month:', popular_month)               
   
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nMost Popular Day:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour                   
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station= df['Start Station'].value_counts().idxmax()
    print('\nMost Common Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station= df['End Station'].value_counts().idxmax()
    print('\nMost Common End Station:', common_end_station)                 


    # TO DO: display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('\nMost frequent start station and end station: ', frequent_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print('\ntotal travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print('\nmean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_stats = df['User Type'].value_counts()
    print('\nUser Types: ', user_stats)


    # TO DO: Display counts of gender    
    try:
        gender_counts = df['Gender'].value_counts()
        print('\ngender type:', gender_counts)
    except KeyError:
        print("\ngender type:\ndata not available.")    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year of Birth:', earliest_year)
    except KeyError:
        print("\nEarliest Year of Birth:\ndata not available.")

        
    try:
        most_recent_year = df['Birth Year'].max()
        print('\nMost Recent Year of Birth:', most_recent_year)
    except KeyError:
        print("\nMost Recent Year of Birth:\ndata not available.")

        
    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year of Birth:', most_common_year)
    except KeyError:
        print("\nMost Common Year of Birth::\ndata not available.")
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_data(df):
    """views raw bikeshare data."""

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
