'''
Basic EDA
'''
import pandas as pd
import numpy as np
raw_data = pd.read_csv('Life Expectancy Data.csv')
# raw_data.sample(n=5).head()
# raw_data.head()
# raw_data.columns
#raw_data.info()
pd.options.display.float_format = '{:.2f}'.format
raw_data.describe().T
# pd.unique(raw_data['Status'])
'''
Data Cleaning
'''
raw_data.rename(columns = {'Country':'country',
                       'Year':'year',
                       'Status':'status',
                       'Life expectancy ':'life_expectancy',
                       'Adult Mortality':'adult_mortality',
                       'infant deaths':'infant_deaths',
                       'Alcohol':'alcohol',
                       'percentage expenditure':'percentage_expenditure',
                       'Hepatitis B':'hepatitis_b',
                       'Measles ':'measles',
                       ' BMI ':'bmi',
                       'under-five deaths ':'under-five deaths',
                       'Polio':'polio',
                       'Total expenditure':'total_expenditure',
                       'Diphtheria ':'diphtheria',
                       ' HIV/AIDS':'hiv/aids',
                       'GDP':'gdp',
                       'Population':'population',
                       ' thinness  1-19 years':'thinness_1_19_years',
                       ' thinness 5-9 years':'thinness_5_9_years',
                       'Income composition of resources':'income_composition_of_resources',
                       'Schooling':'schooling'
                       }, inplace = True, errors = 'raise')
raw_data.drop(raw_data[raw_data['life_expectancy'].isnull()].index, axis=0, inplace=True)
# alcohol
column_alc = ['alcohol']
raw_data.loc[:,column_alc] = raw_data.loc[:,column_alc].bfill()

# Hepatitis
developing_mean = raw_data[raw_data['status']=='Developing'].mean(skipna=True, numeric_only=True).hepatitis_b
#back-filling:
hep_na_ind = raw_data[(raw_data['status'] == 'Developing') & (raw_data['hepatitis_b'].isnull())].index
for row in hep_na_ind:
    raw_data.at[row, 'hepatitis_b'] = developing_mean

# the rest will be front filled:
column_hep = ['hepatitis_b']
raw_data.loc[:, column_hep] = raw_data.loc[:, column_hep].ffill()

# BMI:
raw_data.drop('bmi',axis=1, inplace=True)

# POLIO:
column_pol = ['polio']
raw_data.loc[:, column_pol] = raw_data.loc[:, column_pol].ffill()

# total_expenditure
raw_data.drop(raw_data[raw_data['country']== "Democratic People's Republic of Korea"].index)
column_exp = ['total_expenditure']
raw_data.loc[:, column_exp] = raw_data.loc[:, column_exp].bfill()

# Dipheteria
column_dip = ['diphtheria']
raw_data.loc[:, column_dip] = raw_data.loc[:, column_dip].ffill()

# GDP

#calculating mean to fill
developing_mean = raw_data[raw_data['status'] == 'Developing'].mean(skipna=True, numeric_only=True).gdp
developed_mean = raw_data[raw_data['status']== 'Developed'].mean(skipna=True, numeric_only=True).gdp
# catching rows with null
rows_gdp_null_developing = raw_data[(raw_data['gdp'].isnull()) & (raw_data['status'] == 'Developing')].index
rows_gdp_null_developed = raw_data[(raw_data['gdp'].isnull()) & (raw_data['status'] == 'Developed')].index
#back-filling:
for row in rows_gdp_null_developing:
    raw_data.at[row,'gdp'] = developing_mean
for row in rows_gdp_null_developed:
    raw_data.at[row,'gdp'] = developed_mean

# Population

raw_data.drop('population', axis=1, inplace=True)

# Thinness
deve_mean_1_19 = raw_data[raw_data['status'] == 'Developing'].mean(skipna=True, numeric_only=True).thinness_1_19_years
raw_data['thinness_1_19_years'] = raw_data['thinness_1_19_years'].fillna(deve_mean_1_19)

deve_mean_5_9 = raw_data[raw_data['status']== 'Developed'].mean(skipna=True, numeric_only=True).thinness_5_9_years
raw_data['thinness_5_9_years'] = raw_data['thinness_5_9_years'].fillna(deve_mean_5_9)

# Income composition of resources & Schooling

country_index_d = raw_data[(raw_data['income_composition_of_resources'].isnull())].index

developing_income_mean = raw_data[raw_data['status']=='Developing'].mean(skipna=True, numeric_only=True).income_composition_of_resources
developing_school_mean = raw_data[raw_data['status']=='Developing'].mean(skipna=True, numeric_only=True).schooling

developed_income__mean = raw_data[raw_data['status']=='Developed'].mean(skipna=True, numeric_only=True).income_composition_of_resources
developed_school__mean = raw_data[raw_data['status']=='Developed'].mean(skipna=True, numeric_only=True).schooling

for i in country_index_d:
    if raw_data['status'][i] == 'Developed':
        raw_data.at[i, 'income_composition_of_resources'] = developed_income__mean
        raw_data.at[i, 'schooling'] = developed_school__mean
    if raw_data['status'][i] == 'Developing':
        raw_data.at[i, 'income_composition_of_resources'] = developing_income_mean
        raw_data.at[i, 'schooling'] = developing_school_mean

'''
Save to new csv file
'''
raw_data.to_csv('Life_expec_cleaned.csv', index=False)