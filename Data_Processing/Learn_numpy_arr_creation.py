import numpy as np

array_a = np.ones((3,3),dtype='int64')
array_b = np.zeros((4,4),dtype='int64')

print(array_a)
print(array_b)

print(array_b.dtype)


# Array operation/Manipualtions

array_one =np.array([23,90,110,34],dtype='int64')

print(array_one)
print(array_one + 2)
print(array_one - 5)
print(array_one * 3)
print(array_one / 4)

# array concatenation/addition
a =[5,45,12,90]
b =[23,78,56,12]

c=[a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3]]
print(c)

# Method 2
d=[]   # create the empty list
for i in range(len(a)):
    d.append(a[i]+b[i])
print(d)

#Method 3

array_1a = np.array(a)
array_1b = np.array(b)
print(array_1a.dtype)


print(array_1a + array_1b)
print(type(array_1a + array_1b))

#Concatenate method - union of elements inside each numpy array
print(np.concatenate((array_1a,array_1b)))

 #arange function  range(start,end,counter/skip) for python   arange(start,end,counter/skip)

x=np.arange(2,10,1)

print(x)

y = np.arange(2,20,3)

print(y)

z = np.arange(-10,10,0.5)

print(z)

#reshape

arr_reshape01 =np.arange(4,12).reshape(2,4) # creating numpy array with 2 rows and 4 columns
print(arr_reshape01)  

#arr_reshape02 =np.arange(4,11).reshape(2,4) # creating numpy array with 2 rows and 4 columns
#print(arr_reshape02) 

# reshape for 3 dimensional array

arr_reshape03 = np.arange(24,48).reshape(3,2,4)   # creating numpy array with 3 partitions, 2 rows & 4 columns
print(arr_reshape03)
print(arr_reshape03.ndim)

# reshape for float data type
array_reshape_04 = np.arange(4.,12.,).reshape(4,2)
print(array_reshape_04)

# reshape with dtype
array_int_item = np.arange(1,10,dtype='int16').reshape(3,3)
print(array_int_item)
array_float_item = np.arange(1.55,10.55,dtype='float32').reshape(3,3)
print(array_float_item)

array_float_item_01 = np.arange(1.09,10.09,dtype='float32').reshape(3,3)
print(array_float_item_01)


#random generation
print(np.random.rand(4,3))

print(np.random.randint(-4,10,size=(3,3)))


# Statisical function
arr01 = np.array([89,34,23,100,56,47.6])
print(arr01)

arr02 = np.array([89,34,23,100,56,47])
print(arr02)

print(round(np.mean(arr02),2))

#Median
print(np.median(arr02))

#std devaition
print(round(np.std(arr02),2))

#variance
print(round(np.var(arr02),2))

# Axis - Splitting rows and columns based axes parameters if axis =0 it is column, axis =1 it is row

print(arr_reshape01)  

print(np.sum(arr_reshape01,axis=0))

print(np.sum(arr_reshape01,axis=1))

#sorting
print(np.sort(arr_reshape01))

print(np.sort(arr_reshape01)[::-1])

print(array_one)

print(np.sort(array_one))

print(np.sort(array_one)[::-1])

#Unique
arr02 = np.array([56,23,78,56,100,113,23])
print(arr02)

print(np.unique(arr02))