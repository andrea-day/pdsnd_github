### Date: June 18, 2022

### Title: BikeShare

### Description:
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day. Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used. In this project, I will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## Statistics Computed
#1 Popular times of travel (i.e., occurs most often in the start time)
#most common month
#most common day of week
#most common hour of day

#2 Popular stations and trip
#most common start station
#most common end station
#most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration
#total travel time
#average travel time

#4 User info
#counts of each user type
#counts of each gender (only available for NYC and Chicago)
#earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Data Files:
chicago.csv, washington.csv, new_york_city.csv

### Credits

#def get_filters(df):
https://realpython.com/iterate-through-dictionary-python/
https://stackoverflow.com/questions/53086118/python-for-dummies-using-the-bakeshare-data
https://stackoverflow.com/questions/47495596/combine-multiple-while-statements-python

#def station_stats(df):
https://stackoverflow.com/questions/50848454/pulling-most-frequent-combination-from-csv-columns
https://www.adamsmith.haus/python/answers/how-to-find-the-sum-of-a-pandas-dataframe-column-in-python

#def display_data(df):
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
https://gitlab.com/tomjose1792/BikeShare-Project-Python/-/blob/master/bikeshare.py
