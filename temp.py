import numpy as np
# kanto=np.array([73,12,34])
# weights=np.array([.1 , .3 , .6])
# k=np.dot(kanto,weights)
# print(k)


# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([3,4,5])

# k=np.dot(arr1,arr2,out=None)
# print(k)


# climate_data=np.array([[1,2,3],
#                        [4,5,6],
#                        [7,8,9],
#                        [11,12,13],
#                        [12,34,12]])
# weights=np.array([.5,.7,.6])
# print(climate_data@weights)

# import urllib.request

# urllib.request.urlretrieve(
#     'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv',
#     'climate.txt')
# climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)

# weights = [0.3, 0.4, 0.7]
# yields = climate_data@weights

# climate_results = np.concatenate(
#     (climate_data, yields.reshape(10000, 1)), axis=1)

# np.savetxt('climate_results.txt', climate_results, fmt='%.2f',
#            header='temp,rainfall,humidity,yeild_apples', comments='')


# arr3 = np.array([
#     [[11, 12, 13, 14],
#      [13, 14, 15, 19]],

#     [[15, 16, 17, 21],
#      [63, 92, 36, 18]],

#     [[98, 32, 81, 23],
#      [17, 18, 19.5, 43]]])
# arr3[1,1,3] gives 18               arr3[1: , 1 ,3]  gives [18,43]


# arr1 = list(range(1000000))
# arr2 = list(range(1000000, 2000000))
# arr1_np = np.array(arr1)
# arr2_np = np.array(arr2)
# print(np.dot(arr1_np, arr2_np))


# arr = np.random.rand(5)
# print(arr)
# np.mean(arr)

# arr = np.array([[1, 2, 3],
#                [3, 5, 7]])
