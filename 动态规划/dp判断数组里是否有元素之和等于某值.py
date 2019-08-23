import numpy as np
#给你一个列表，再给你一个数，
#判断列表中是否有若干个元素之和等于这个数
#s指的是前面是否有若干数之和等于s

arr = [3,34,4,12,5,2]
arr3 = [1,2,3,4,5,6]
def rec_subset(arr,i,s):
    if s == 0:
        #如果等于0了，说明之前的过程已经完成使命了
        return True
    elif i == 0:
        #这是最后的机会了，如果再不等于s就宣告失败了
        return arr[0] == s
    elif arr[i] > s:
        #那么肯定不能选元素i了，因为超重了
        return rec_subset(arr,i-1,s)
    else:
        A = rec_subset(arr,i-1,s-arr[i])  #选
        B = rec_subset(arr,i-1,s)  #没选
        return A or B
        #这个or，说的是两条路，只要一条路走得通就成立了

print(rec_subset(arr,len(arr)-1,9))
print(rec_subset(arr,len(arr)-1,10))
print(rec_subset(arr,len(arr)-1,11))
print(rec_subset(arr,len(arr)-1,12))
print(rec_subset(arr,len(arr3)-1,20))

'''如何用动态规划呢？用一个二维数组来保存中间的过程
      s  0 1 2 3 4    5 6 7 8 9 
arr i
3   0   T F F T F    F F F F F
34 1   T
4   2   T
12 3   T
5   4   T
2   5   T
显然，第一排基本都是F
第一列全是T，因为使命都完成了
'''
arr3 = [1,2,3,4,5,6]
def dp_subset(arr,ss):
    subset = np.zeros((len(arr),ss+1),dtype=bool)
   
    subset[0,:] = False
    subset[:,0] = True
    subset[0,arr[0]] = True
    #开始填表格的剩下部分
    for i in range(1,len(arr)):
        for s in range(1,ss+1):
            if arr[i]>s:
                subset[i,s]=subset[i-1,s]
            else:
                A = subset[i-1,s-arr[i]]
                B = subset[i-1,s]
                subset[i,s]=A or B
    r,c = subset.shape
    return subset[r-1,c-1]
print("***")
print(dp_subset(arr,9))
print(dp_subset(arr,10))
print(dp_subset(arr,11))
print(dp_subset(arr,12))
print(dp_subset(arr3,20))
print("***")


for q in range(1,23):
    print(dp_subset(arr3,q),end=' ')
