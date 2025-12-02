import numpy as np
import pandas as pd

df = pd.read_csv(r'Countries.csv')
# print(df[df['population'] == df['population'].max()]['capital_city'])

# print(df[df['population']== df['population'].min()]['capital_city'])
# print(df.sort_values(by = 'democracy_score',ascending=False,inplace=True))
# print(df['country'].head())

# print(df['region'].value_counts().count())

# print(df['region'].value_counts() ['Eastern Europe'])

# print(df[df['population']== df['population'].nlargest(2).iloc[1]]['political_leader'])
# print(df[df['political_leader'].isna()]['country'])


# count = 0

# def Counting(txt):
#     global count
#     if 'republic' in txt.lower():
#         count += 1
#     return txt

# df['country_long'] = df['country_long'].apply(Counting)
# print(df['country_long'])    


african_df = df[df['continent']=='Africa']
print(african_df[african_df['population']==african_df['population'].max()])