import pandas as pd
data={'Name':['Alice','Bob','Charlie'],
      'Age':[25,30,35],
      'City':['New York','San francisco','Los Angeles']      
      }
df=pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\n Age column:") 
print(df['Age'])
print("\n Row at index 1:")
print(df.iloc[1])
