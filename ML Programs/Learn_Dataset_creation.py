# Parameters - area, bedrooms, age,price

import numpy as np
import pandas as pd

# Seed - to reproduce the random number generation properly and consistent data

np.random.seed(10)

n=100

area = np.random.randint(500,2400,n)
bedrooms =np.random.randint(1,4,n)
build_age=np.random.randint(1,20,n)
price =(area*125+ bedrooms*12000-build_age*1500+np.random.normal(0,20000,n))

df01 = pd.DataFrame({
     "area":area,
     "bedrooms":bedrooms,
     "building_age":build_age,
     "price":price.astype(int)
})

print(df01.head())

# Save to csv
df01.to_csv("D:\housing_price_details.csv",index=False)