import numpy as np

print("numpy version is:",np.__version__)

#1D Array

print(np.array([10,20,40,67]))

#2D Array

array_2d =np.array([[45,67],[34,103]])
print(array_2d)
print(type(array_2d))

#3D Array

array_3d =np.array([[[45,67],[34,103]],[[15,27],[14,19]]])
print(array_3d)
print(type(array_3d))


# array attributes
# array dimension
print(array_2d.ndim)
print(array_3d.ndim)

#size of the array
print(array_2d.shape)
print(array_3d.shape)

# items/no of elements in the array
print(array_2d.size)
print(array_3d.size)

#dtype
print(array_2d.dtype)
print(array_3d.dtype)

#itemsize
print(array_2d.itemsize)
print(array_3d.itemsize)
