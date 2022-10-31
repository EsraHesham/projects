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
    while True:

        city= input('Would you like to see data for Chicago, New york city ,or Washington?\n').lower()
        if city not in ['chicago', 'new york city' , 'washington']:
            print('INVAILD INPUT!!')
            continue

        else:
            choice= input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n').lower()

            if  choice == 'month':
                month = input('Which month? January, February, March, April, May, or June?\n').lower()
                if month not in ['january', 'february', 'March', 'april', 'may', 'june']:
                    print ('Invalid Input!!')
                    continue

                day='all'
                break

            elif choice == 'day':
                day = input('Which day? sunday, monday, tuesday, wednesday, thursday,or friday.\n').lower()
                month='all'
                if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
                    print ('Invalid Input!!')
                    continue
                break

            elif choice == 'both':
                month = input('Which month? January, February, March, April, May, or June?\n').lower()
                if month not in ['january', 'february', 'March', 'april', 'may', 'june']:
                    print ('Invalid Input!!')
                    continue
                day = input('Which day? sunday, monday, tuesday, wednesday, thursday,or friday.\n').lower()
                if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
                    print ('Invalid Input!!')
                    continue
                break
            elif choice == 'none':
                month='all'
                day='all'
                break
            else:
                print ('Invalid Input!!')


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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
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

        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']== day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['month'] =df['Start Time'].dt.month_name()
    popular_month = df['month'].mode()[0]
    print ('The most common month: {}.'.format(popular_month))

    df['day_of_week'] =df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print ('The most common day: {}.'.format(popular_day))

    df['hour'] =df['Start Time'].dt.hour

# find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print ('The most common hour {}.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    popular_start_Station= df['Start Station'].mode()[0]
    counts = df['Start Station'].value_counts()[0]
    print ('The most common start_Station : {}, Counts= {}.'.format(popular_start_Station,counts))

    popular_end_Station= df['End Station'].mode()[0]
    counts_end = df['End Station'].value_counts()[0]
    print ('The most common end_Station : {}, Counts= {}.'.format(popular_end_Station,counts_end))


    combination=df.groupby(['Start Station','End Station']).size().idxmax()
    counts_combination=df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)[0]
    print ('The most common combination of start station and end station trip : {}, Counts= {}.'.format(combination,counts_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_time= df['Trip Duration'].sum()
    print('The total travel duation : {}.'.format(total_time))

    avg_time= df['Trip Duration'].mean()
    print('The mean travel duation : {}.'.format(avg_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    counts_user_types= df['User Type'].value_counts()
    print(counts_user_types)
    try:
        counts_gender= df['Gender'].value_counts()
        print(counts_gender)
    except:
        print('No Gender Data.')

    try:
        earliest_year= df['Birth Year'].min()

        most_recent_year= df['Birth Year'].max()

        most_common_year= df['Birth Year'].mode()[0]
        print("earliest_year, most_recent_year,and most_rcommon_year: {}, {}, {}.".format(earliest_year,most_recent_year,most_common_year))
    except:
        print('NO Birth Data.')


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

        display= input('\nWould you display? Enter yes or no.\n')
        while (display.lower() == 'yes'):

            print(df.sample(n=5))
            display= input('\nWould you like to see individual trip data? Enter yes or no.\n')


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
