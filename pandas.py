from IPython.display import display
import pandas as pd
from urllib.request import urlretrieve
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')
urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv',
            'locations.csv')


covid_df = pd.read_csv('italy-covid-daywise.csv')
locations_df = pd.read_csv('locations.csv')

initial_tests = 935310
total_tests = initial_tests + covid_df.new_tests.sum()
# gives all info
# covid_df.info()

# # gives min max mean etc
# covid_df.describe()

# # gives header
# covid_df.coloumns()


# # gives all the new cases
# covid_df['new_cases']

# # gives specific values at that index
# covid_df.at[190, 'new_cases']


# # gives two coloumns at same time
# covid_df[['date', 'new_cases']]

# covid_df_copy = covid_df.copy


# # gives row information
# covid_df.loc[190]

# # covid_df.head(10) gives first rows
# # covid_df.tail(20)  gives last 20 rows

# # covid_df.loc[108:120]  prints range

# # covid_df.sample(10)  random rows


# covid_df.new.cases.sum()


# # querrying and sorting
# # display 100 rows
# high_new_cases = covid_df.new_cases > 1000
# with pd.option_context('display.max_rows', 100):
#     display(covid_df[covid_df.new_cases > 1000])

# # sort colums
# covid_df.sort_values('new_cases')

# covid_df.at[172, 'new_cases'] = (
#     covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases'])/2

# # update any value
# covid_df.at[2, "new_cases"] = 4


#  DATES

covid_df['date'] = pd.to_datetime(covid_df.date)

# Converting into date type format

covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

# print(covid_df[covid_df.month == 5])


# summing o particular coloumns
covid_df_may = covid_df[covid_df.month == 5]
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests',]]

# print(covid_df_may_metrics)
# print(covid_df_may_metrics.sum())

#  same in single statment

k = covid_df[covid_df.month == 5][[
    'new_cases', 'new_deaths', 'new_tests']].sum()

#  average of new cases
a = covid_df.new_cases.mean()

# lets average of sundays

p = covid_df[covid_df.weekday == 6].new_cases.mean()

# average of everything

p1 = covid_df[covid_df.weekday == 6][[
    'new_cases', 'new_deaths', 'new_tests']].mean()


# GROUPS
monthly_groups = covid_df.groupby('month')
q1 = monthly_groups[['new_cases', 'new_deaths', 'new_tests']].sum()

weekly_grp = covid_df.groupby('weekday')[['new_cases', 'new_deaths']].mean()


#  Added a file locations.csv

#  seeing data of italy only
# print(locations_df[locations_df.location == 'Italy'])

# Adding italy to covid df
covid_df['location'] = "Italy"


# MERGING DATA FRAMES


covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests

merged_df = covid_df.merge(locations_df, on="location")

merged_df['cases_per_million'] = merged_df.total_cases * \
    1e6 / merged_df.population
merged_df['deaths_per_million'] = merged_df.total_deaths * \
    1e6 / merged_df.population

merged_df['tests_per_million'] = merged_df.total_tests * \
    1e6 / merged_df.population
# Creating small    table with required

result_df = merged_df[['date',
                       'new_cases',
                       'total_cases',
                       'new_deaths',
                       'total_deaths',
                       'new_tests',
                       'total_tests',
                       'cases_per_million',
                       'deaths_per_million',
                       'tests_per_million']]
#  Saving to a csv file

result_df.to_csv('results.csv', index=None)

# result_df.new_cases.plot()

# covid_df.new_tests.plot()


result_df.set_index('date', inplace=True)

result_df.new_cases.plot()
result_df.new_deaths.plot()
