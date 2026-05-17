import numpy as np
import matplotlib.pyplot as plt

x1=np.array([160,168,170,175,180,184,190])
y1=np.array([49,55,54,62,64,60,71])

x2=np.array([145,162,171,165,170,174,185])
y2=np.array([54,59,64,68,74,70,79])

plt.scatter(x1,y1,color='blue',label='Group1')
plt.scatter(x2,y2,color='green',label='Group2')
plt.title("Comparison of 2 groups for BMI Index")
plt.xlabel("Height in cm(s)")
plt.ylabel("Weight in Kg(s)")
plt.show()