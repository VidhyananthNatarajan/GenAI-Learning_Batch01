import matplotlib.pyplot as plt

fruits =['Apples','Mango','Dates','Grapes','Banana']
sales =[400.5,376.67,290.75,441.70,399.50]

plt.bar(fruits,sales,color='blue',width=0.5)
plt.title("Sales Analysis of Fruits")
plt.xlabel('Fruits')
plt.ylabel("Sales in Thousands")
plt.show()

plt.barh(fruits,sales,color='blue')
#plt.bar(fruits,sales,color='blue',width=0.5)
plt.title("Sales Analysis of Fruits")
plt.xlabel('Fruits')
plt.ylabel("Sales in Thousands")
plt.show()