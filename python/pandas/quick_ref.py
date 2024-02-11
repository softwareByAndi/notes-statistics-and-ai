import re
import pandas as pd

input_data_path = '../test_data/test_data.csv'
data_output_dir = '../test_data/25_best_practices/'
def fix_column_names(name):
    name = re.sub(r'[\s\-/]', '_', name) # Replace whitespace & - characters with '_'d
    name = re.sub(r'[^\w\s]', '', name) # Remove all non-alphanumeric characters except '_'
    return name.lower()

df = (
    pd.read_csv(
        input_data_path, 
        index_col=['ID'],
        parse_dates=['Birthday']
    )
    .rename(columns=fix_column_names)
    # .rename(columns={'Name': 'name', 'Age': 'age', ... })
)

# df.to_csv('path/to/data.csv', index=False)
# df.to_excel('path/to/data.xlsx', index=False)
# large_df.to_parquet('path/to/data.parquet')
# large_df.to_feather('path/to/data.feather')
# large_df.to_pickle('path/to/data.pickle')

print('\n\n\nHEAD & TAIL:')
print(df.head(3))
print(df.tail(3))
print('\nINFO:')
print(df.info())
print('\nDESCRIBE:')
print(df[['age', 'salary']].describe().T)
print('\n-------------------\n')

salary_limit = df['salary'].quantile(0.95)
df['test'] = df['salary'] > salary_limit
print(df.test.value_counts())
df = df.drop(columns=['test'])
print(df.columns)

print(
    df.plot(
        kind='scatter',
        x='age', 
        y='salary',
        title='age vs salary'
    )
)

print('max age:', df['age'].max())
print('min age:', df['age'].min())
age_limit = df.age.quantile(0.5)
avg_salary = (
    df
    .query('age > @age_limit') # just for example purposes
    .assign(
        age_group=(df['age'] * 2 / 10) # every 5 years
            .astype('int32') # floor
            * 5
        # age_group=lambda x: np.where(x['age'] < age_limit, 'young', 'old')
        # age_group=(df['age'] < age_limit).map({True: 'young', False: 'old'})
    )
    .groupby('age_group')
    ['salary']
    # .describe()
    .agg(['mean', 'median', 'std'])
    # .agg(['mean', 'count', 'std', 'min', 'max', 'median', 'sum', 'sem', 'var', 'skew'])
    .round(2)
    .assign(
        perc_change=lambda x: x['mean'].pct_change(),
        diff=lambda x: x['mean'].diff()
    )
)
# avg_salary['perc_change'] = avg_salary['mean'].pct_change()
# avg_salary['diff'] = avg_salary['mean'].diff()

print(avg_salary)