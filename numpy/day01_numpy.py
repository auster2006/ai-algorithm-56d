import numpy as np
a = np.array([1,2,3,4,5])
print(a)
print(type(a))

b = np.zeros((3,4))
print(b)

c = np.ones((2,3))
print(c)

d = np.arange(0,10,2)
print(d)

e = np.array([1, 2, 3, 4, 5, 6])
f = e.reshape(2, 3)
print(f)

g = e.reshape(6,1)
print(g)

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(A[1,2])
print(A[:,:])

print(A>6)

print(A[A>6])

print(A+10)

print(A*2)

print(A**2)

B = np.ones((3, 4))

print(A + B)
print(A * B)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.sum())
print(A.mean())
print(A.max())
print(A.min())

print(A.sum(axis=1))

print(A.T)

print(A @ B)