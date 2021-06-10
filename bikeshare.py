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

    valid_cities=['chicago', 'new york city', 'washington']
    while(True):
        city=input('Please enter a city from (chicago, new york city, washington): ')
        if city.lower() in valid_cities:
            break
        else:
            print('invalid input, please try again')



    months=['all','january','february','march','april','may','june']

    while(True):
        month=input('Please enter a month from (all, january, february, march, april, may, june): ')
        if month.lower() in months:
            break
        else:
            print('invalid input, please try again')



    week_days=['all','monday', 'tuseday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while(True):
        day=input('Please enter a day of week (all, monday, tuseday, wednesday, thursday, friday, saturday, sunday): ')
        if day.lower() in week_days:
            break
        else:
            print('invalid input, please try again')



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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])

    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour

    if month!='all':
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)+1
        df=df[df['month']==month]
    return df

    if day!='all':
        df=df[df['day_of_week']==day.title()]


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    popular_month=df['month'].value_counts().idxmax()
    print('The most common month is: ', popular_month)


    popular_day_of_week=df['day_of_week'].value_counts().idxmax()
    print('The most common day of week is: ', popular_day_of_week)


    popular_hour=df['hour'].value_counts().idxmax()
    print('The most common start hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    popular_start_station=df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ', popular_start_station)


    popular_end_station=df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: ', popular_end_station)


    df['start end stations']='start station: '+df['Start Station']+", end station: "+df['End Station']
    popular_start_end_station=df['start end stations'].value_counts().idxmax()
    print('The most commonly used combination of start station is: ', popular_start_end_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()



    df['Total travle time']=pd.to_datetime(df['End Time'])-df['Start Time']

    print("Total travle time: ")
    print(df['Total travle time'].sum())


    print("mean travle time: ")
    print(df['Total travle time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    view_data=input('Would you like to view 5 rows of individual trip data? Enter yes or no: ').lower()
    while (view_data!='no' and view_data!='yes'):
        print('Invalid input, please try again')
        view_data=input('Would you like to view 5 rows of individual trip data? Enter yes or no: ').lower()
    start_loc=0
    while (view_data.lower()=='yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc+=5
        view_data=input('Do you wish to continue? Enter yes or no: ').lower()
        while (view_data!='no' and view_data!='yes'):
            print('Invalid input, please try again')
            view_data=input('Do you wish to continue? Enter yes or no: ').lower()



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    user_types = df['User Type'].value_counts()
    print("Counts of user typse:")
    print(user_types)


    gender = df['Gender'].value_counts()
    print("Counts of gender:")
    print(gender)

    
    print("Earliest year of birth: ", int(df['Birth Year'].min()))
    print("Most recent year of birth: ", int(df['Birth Year'].max()))
    print("Most common year of birth: ", int(df['Birth Year'].value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
