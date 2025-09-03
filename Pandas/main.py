import pandas as pd

df = pd.read_csv('pokemon_data.csv')
#print(df.head(3))

#df_xlsx = pd.read_excel('pokemon_data.xlsx')
#print(df_xlsx.head(3))

#df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')
#print(df_txt.head(3))

#print(df.columns)
#print(df['Name'])
#print(df['Name'][0:5])
#print(df[['Name','Type 1']])

#print(df.iloc[0:4])

#print(df.iloc[2,1])

#for index, row in df.iterrows():
#   print(index,row['Name'])

#print(df.loc[df['Type 1'] == "Fire"])

#print(df.describe())

print(df.sort_values('Name', ascending=False))