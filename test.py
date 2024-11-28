import pandas as pd

df = pd.read_csv("./test_data/Flavors.csv")
group_by_frame = df.groupby('Base Flavor')
print(df)
print(group_by_frame.agg({'Texture Rating':['mean','min','max','sum'],'Total Rating':['mean','min','max','sum']}))