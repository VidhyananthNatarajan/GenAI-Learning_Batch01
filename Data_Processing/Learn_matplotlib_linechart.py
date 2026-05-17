import matplotlib.pyplot as plt

days =['Mon','Tue','Wed','Thurs','Fri','Sat','Sun']
temp =[26.4,28.9,30.1,32.7,29.9,33.0,32.6]

plt.plot(days,temp,marker='o')
plt.title("Weekly temperature")
plt.xlabel("Days")
plt.ylabel("Temperature in celsius")
plt.show()