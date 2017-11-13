# 
import K_means as K

arrOrigin = [[1, 7], [1, 6], [1, 5], [2, 3], [2, 2], [3, 1], [4, 1], [5, 2], [5, 3], \
             [7, 5], [7, 6], [7, 7]]  # input arguments
k = 3  # the number of clusters   k <= data size

[belong, center] = K.K_means(arrOrigin, k)