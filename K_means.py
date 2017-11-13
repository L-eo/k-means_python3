# K-means Cluster
# This thought from four picture of Wikipedia's k-means clustering
# The webside: https://en.wikipedia.org/wiki/K-means_clustering  (in 3.1.1 Initialization methods)
# 2017-11-10 09:37:52
# input parameter: a numerical matrix, int
#                  matrix's row is on behalf of data characteristics
#                  matrix's column is on behalf of data size
#                  the int of the second parameter must be less than the matrix's column of the first one.
# output parameter: two one-dimensional vectors
#                   the first vector is on behalf of the cluster of the data's point
#                   the second one is the cluster's center.

import random
import fmaxmin
import distance as dis

def K_means(arr, k):
    if(type(arr)==list and type(k)==int):  # check input parameter
        if(k <= len(arr) and k>=1):
            1
        else:
            print('Error, "k>=1 and k<=data size" that must be satisfied.')
            return -1
    else:
        print("Error, input parameter isn't match.")
        return -1

    dim = len(arr[0])
    num = len(arr)
    [v_min, v_max] = fmaxmin.fmaxmin(arr)
    center = [[0 for col in range(dim)] for row in range(k)]
    while 1:
        for i in range(k):
            for j in range(dim):
                center[i][j] = v_min[j] + random.random()*(v_max[j]-v_min[j])
#         center = [[1,1], [3,3], [5,5]]
        belong = [0 for col in range(num)]  # record every point belong to which cluster
        dis_k = [-1 for col in range(k)] # record the distance between every point and the center
        for i in range(num):
            for j in range(k):
                dis_k[j] = dis.dis(center[j], arr[i])
            belong[i] = dis_k.index(min(dis_k))
        flag = 0
        for i in range(num): # if someone cluster is none point, we must re-distribute
            if(belong[i] == -1):
                flag = 0
            else:
                flag += 1
        if(flag == num):
            break  # until now, the initialization has been finished. 
                   # In other words, the second picture has been finished of the four picture in wiki.
                   
    center2 = [[0 for col in range(dim)] for row in range(k)]
    time = 0   # times of iteration
    while(time<100):
        center2 = center[:]
        for i in range(k):
            temp_p = []
            for j in range(num):
                if(belong[j] == i):
                    temp_p.append(arr[j])
            center[i] = dis.center_mass(temp_p)
        flag = 0
        for i in range(k):
            if(dis.dis(center2[i], center[i]) < 1e-4):
                flag += 1
            else:
                for i in range(num):
                    for j in range(k):
                        dis_k[j] = dis.dis(center[j], arr[i])
                    belong[i] = dis_k.index(min(dis_k))
        if(flag == k):
            break
        else:
            time += 1

    print(belong)
    print(center)
    # print(time)
    return(belong, center)
