import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ('chicago', 'new york city', 'washington')

months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')   

days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
          city = input("Please choose a city to review: Chicago, New York City, or Washington. \n>>> ").lower()
          if city in cities:
              break
          else:
              print('Please choose a different city.')
    print(f"\nYou have chosen {city.title()} as your city. \n")
    
    # get user input for month (all, january, february, ... , june)

    while True:
            global month
            month = input("Please choose a month between January and June or All. \n>>> ").lower()
            if month in months:
                break
            else:
                print('Please choose a different month.')
    print(f"\nYou have chosen {month.title()} as your month. \n")
    
    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
            day = input("Please choose a day of the week (full name) or All. \n>>> ").lower()
            if day in days:
                break
            else:
                print('Please choose a different day.')
    print(f"\nYou have chosen {day.title()} as your day. \n")
    
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
    print(f"\nLoading the data using {city.title()}, {month.title()}, {day.title()}. \n")
    print('Reading the CSV file. \n')
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day_of_Week'] == day.title()]
        
    print("Head Info: ", df.head(), "\n")
    print("Column Info: ", df.columns, "\n")
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Uses mode method to find the most popular month
    popular_month = df['Month'].mode()[0]
    
    half_year = {
                1 : "January",
                2 : "February",
                3 : "March",
                4 : "April",
                5 : "May",
                6 : "June"
            }

    for key, value in half_year.items():
        if popular_month == key:
           print("The most common month is: {}" .format(value))

    #Uses mode method to find the most popular day
    popular_day = df['Day_of_Week'].mode()[0]
    
    
    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].value_counts().idxmax()


    print("The most common day of the week is: {} \n"
          "The most common hour is: {}:00".format(popular_day, popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    popular_combo = df.groupby(['Start Station','End Station']).size().nlargest(1)

    print("The most common Start Station is: {} \n" 
          "The most common End Station is: {} \n"
          "The most common hour is: {}".format(popular_start, popular_end, popular_combo))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time_hrs = round(df['Trip Duration'].sum() / 60 /60, 2)

    # display mean travel time
    mean_travel_time_min = round(df['Trip Duration'].mean() / 60,2)

    print('The total travel time in hours is: {} \n'
          'The average travel time in minutes is: {}'.format(total_travel_time_hrs, mean_travel_time_min))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()

    # Display counts of gender
    # gender_count = df['Gender'].value_counts()
    
    try:
        gender_count = df['Gender'].value_counts()
        print('The count break down of User Types is: {} \n'
               'The count break down of Genders is: {} \n'.format(user_type_count, gender_count))
    except:
        print("\nThere is no 'Gender' column in this file.")

    # Display earliest, most recent, and most common year of birth
    try:
        min_year = int(df['Birth Year'].min())
        max_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('The earliest Birth Year is: {} \n'
              'The most recent Birth Year is: {} \n'
              'The most common Birth Year is: {}'.format(min_year, max_year, common_year))
    except:
        print("\nThere is no 'Birth Year' column in this file." )
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Asks for user input to determine if 5 rows of the Dataframe should be displayed.
    
    Continues to ask for user input until the user exits the function."""
    while True:
        data_rows = input("Would you like to view 5 rows of data? (Yes or No)\n>>>").lower()
        if data_rows == 'yes':
            row_start = 0
            row_end = 5
            rows = df.iloc[row_start:row_end]
            print(rows)
            break  
        elif data_rows == 'no':
            break
        else:
            print("Please try again.\n")
    if data_rows == 'yes':       
            while True:
                more_rows = input("Would you like to view 5 additional rows of data? (Yes or No)\n>>>").lower()
                if more_rows == 'yes':
                    row_start += 5
                    row_end += 5
                    rows = df.iloc[row_start:row_end]
                    print(rows)
                elif data_rows == 'no':
                    break
                else:    
                    print("Please try again.\n")  
            else:
                print("Please try again.\n")    

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
