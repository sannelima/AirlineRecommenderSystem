import pandas as pd
excel_filename ='capstone_airline_reviews3.xlsx'
csv_name = 'capstone_reviews.csv'

df_main = pd.read_excel('capstone_airline_reviews3.xlsx')
df_main = df_main.dropna(subset=['airline'])

df_main.to_csv(csv_name, index=False)
