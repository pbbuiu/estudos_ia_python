import numpy as np

arr = np.array([[1, 2, 3, 4, 0], [6, 7, 8, 9, 10]])

x = arr.view()
x[0, :2] = 34

print(x)
print(arr)

if x.base is not None:
    print("Esse dado não pertence a x")

print(x.ndim)
print(x.shape)

arr2 = np.array([[1, 8, 3, 5, 2], [7, 12, 10, 13, 2]], ndmin=1)
print(arr2.shape)
print(arr2)

for x in arr:
    print('{', end='')
    for y in x:
        print(y, end=' ')
    print('}')

for x in np.nditer(arr):
    print(x, end=' ')

for idx, x in np.ndenumerate(arr):
    print(idx, x)

newarr = np.concatenate((arr, arr2,), axis=1)

for x in np.nditer(newarr):
    print(x, end=' ')
print()
arrRange = np.arange(9, 15, dtype='i')
newRange = arrRange.reshape(2, 3)
print(arrRange)
print(newRange)

# print(dir(np.arange))
# print(help(np.linspace))

arrLinspace = np.linspace(0, 10, num=5, dtype='i')
print(arrLinspace)

arrLinspace += 2 #broadcasting
print(arrLinspace)
arrLinspace *= 2 #broadcasting
print(arrLinspace)
# arrLinspace = arrLinspace/int(2) #broadcasting
# print(arrLinspace)
mulplyArr = arrLinspace * arr
p2 = np.array([2, 4], dtype='i')

print(arrLinspace)
print(arr)
print(mulplyArr)

randomArr = np.random.default_rng()
print()
arrR = randomArr.integers(0, 10, 15)
print(arrR)