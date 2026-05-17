import pandas as pd

dict01={"key1":["value01","value02","value03"],"key2":["value04","value05","value06"]}
print(dict01)

data = pd.DataFrame(dict01)
print(data)


data_01 ={"user01":["I Liked it","Taste was good"],"user02":["Pretty Good","Ok. Need improvement"]}
print(data_01)
df02 = pd.DataFrame(data_01)
print(df02)
df01 = pd.DataFrame(data_01,index=["ice cream","Apple juice"])
print(df01)

# reading the values

#df_csv_read = pd.read_csv("D:\customer.csv")
#print(df_csv_read)

#df_excel_read = pd.read_excel("D:\Data Analyst\Sales Data.xlsx")
#print(df_excel_read)

df_json_read = pd.read_json("D:\data_json.json")
print(df_json_read)