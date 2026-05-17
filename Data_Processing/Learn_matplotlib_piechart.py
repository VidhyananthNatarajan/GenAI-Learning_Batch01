import matplotlib.pyplot as plt

Car_brands =['AUDI','HYUNDAI','FORD','TESLA','JAGUAR']
sales_data =[23,17,35,29,12]

plt.pie(sales_data,labels=Car_brands)
plt.show()