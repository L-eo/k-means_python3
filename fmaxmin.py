# find max and min value according to dimension
# input parameter: the matrix
# output parameter: two vector :the minimum vector and the maximum vector

def fmaxmin(a = [[0,0],[1,1],[2,2]]):
    num = len(a);
    dim = len(a[0]);
    max_ver = a[0][:];
    min_ver = a[0][:];
    for i in a:
        for j in range(dim):
            if(i[j] > max_ver[j]):
                max_ver[j] = i[j]
            if(i[j] < min_ver[j]):
                min_ver[j] = i[j]
    
    return (min_ver, max_ver)