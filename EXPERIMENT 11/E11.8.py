import pandas as pd
df_csv=pd.read_csv("Sample.csv")
print("Data Frame from csv:")
print(df_csv)
df_json=pd.read_json('Sample.json')
print("\n Data Frame from JSON:\n",df_json)