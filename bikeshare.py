import time
import pandas as pd
import numpy as np

# CITY_DATA is used to store names of the files that store the information.
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
    cities = ['Chicago','New York City','Washington']
    months = ['All','January','February','March','April','May','June']
    days = ['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
  
    print('Hello! Let\'s explore some US bikeshare data!')
  
    while True:
        try:
            # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            city = cities.index(input("Please, type the name of the city [chicago, new york city, washington]: ").lower().title())

            # TO DO: get user input for month (all, january, february, ... , june)
            month = months.index(input("#You can use \"all\" to select all months\nPlease, enter the name of the month(January - June): ").lower().title())

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = days.index(input("#You can use \"all\" to select all days\nPlease, enter the name of the day: ").lower().title())
            
            break
        except ValueError:
            print("ERROR! You have entered wrong values!")
    
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
    """
    Since the CITY_DATA dictionary is unordered and cannot be indexed,
    I got the values (which are the name of the files) and stored them in a list, so I can iterate through it with ease.
    """
    # Takes dictionary values.
    files = CITY_DATA.values() 
    
    # Stores them in a list.
    files_list = list(files) 
    
    df =  pd.read_csv(files_list[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
        
    days = ['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
   
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
   
    pop_month = df['month'].mode()[0]

    print('Most Popular Start Month:', pop_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
   
    pop_day = df['day_of_week'].mode()[0]

    print('Most Popular Start Day:', pop_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
   
    pop_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', pop_hour)

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_st = df["Start Station"].mode()[0]
    print("Most commonly used start station is {}".format(pop_start_st))

    # TO DO: display most commonly used end station
    pop_end_st = df["End Station"].mode()[0]
    print("Most commonly used end station is {}".format(pop_end_st))

    # TO DO: display most frequent combination of start station and end station trip
    pop_comb_st = df.groupby(["Start Station", "End Station"]).size().nlargest(1)
    print("Most frequent trip is ", pop_comb_st)

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df["Trip Duration"].sum()
    print("Total travel time is {} hours".format(int(tot_travel_time%3600)))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Travel time mean is %s seconds" % round(mean_travel_time,2))

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df["User Type"].value_counts()
    print(user_count)
    
    # Checks if coulmn "Gender" exists in the panda dataframe becasue it does not exist in washington.csv
    if "Gender" in df.columns:
        # TO DO: Display counts of gender
        gender_count = df.Gender.value_counts()
        print(gender_count)
    # Checks if coulmn "Birth Year" exists in the panda dataframe becasue it does not exist in washington.csv
    if "Birth Year" in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df["Birth Year"].mode()[0]
        print("\nMost common birth year is {}".format(int(birth_year)))
        earliest_year = df["Birth Year"].min()
        print("\nEarliest birth year is {}".format(int(earliest_year)))
        recent_year = df["Birth Year"].max()
        print("\nMost recent birth year is {}".format(int(recent_year)))
        

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)
# I created this function to display the next five records if  a user wants to.
def display_record(df):
    
    """
    Loads data for the specified city and the choice of the user to display a sample data or not.

    Args:
        (str) choice - a single character (y = yes, n = no)
    Returns:
         prints five consecutive records of the dataframe.
    """
    index = 0
    choice = str(input("Would you like to see a sample of the data? [y/n]: ").lower())
    pd.set_option('display.max_columns',200)
    while True:
        
        if choice == 'y':
            print(df.iloc[index:index+5, 0:])
            choice = str(input("Would you like to see a sample of the data? [y/n]: ").lower())
            index+=5
          
        elif choice == 'n':
            break
        else:
            print("Wrong value!")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)    
        display_record(df)

        
        restart = str(input('\nWould you like to restart? Enter yes or no.\n'))
        if restart.lower() == 'yes':
            continue
        elif restart.lower() == 'no':
            break
        else:
            print("Wrong value!")
            break
               
        


if __name__ == "__main__":
	main()
