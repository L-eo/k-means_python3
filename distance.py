# distance of two point or center of mass of some points
# It use quadratic sum and means simply, you can use differernt equation as your question

import math
def dis(a, b):
    sum = 0;
    for i in range(len(a)):
        sum += math.sqrt((a[i]-b[i]) * (a[i]-b[i]))
    return sum

def center_mass(a):
    long = len(a)
    dim = len(a[0])
    ret = [0 for col in range(dim)]
    for i in range(dim):
        avg = 0
        for j in range(long):
            avg += a[j][i]
        ret[i] = avg/long
    return ret