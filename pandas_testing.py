import pandas as pd

# df = pd.read_csv("./test_data/world_population.csv")
# pd.set_option('display.max.rows',235)
# # df.set_index(['Continent','Country'],inplace= True)
# # df.sort_index(ascending=[False,True],inplace=True)
# print(df)
#


df = pd.read_excel('./Excels/maha.xlsx',index_col=False)
print(df[df['STATUS'].str.contains('WIP')])