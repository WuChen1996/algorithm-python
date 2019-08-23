#import numpy as np
#一串数组，挑选出里面的元素，使得和最大。元素不能相邻。
arr = [1,2,4,1,7,8,3]
arr2 = [1,2,3,4,5,6,7,100]
arr3 = [4,1,1,9,1]

#opt(i)是指
#max{opt(i-2)+arr[i] （代表选了i元素）, opt(i-1) （代表没选）}
def rec_opt(arr,i):
    if i == 0 :
        #即:opt[0]=arr[0] , 既然只有一个，肯定要选咯
        return arr[0]
    elif i ==1:
        return max(arr[0],arr[i])
        #二选一，肯定选最大的咯
    else:
        A=rec_opt(arr,i-2)+arr[i]
        B=rec_opt(arr,i-1)
        return max(A,B)

print(rec_opt(arr,6))
print(rec_opt(arr2,7))
print(rec_opt(arr3,4))

def dp_opt(arr):
    #opt = np.zeros(len(arr))
    opt=[0]*len(arr)
    opt[0]=arr[0]
    opt[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        A=opt[i-2]+arr[i]
        B=opt[i-1]
        opt[i] = max(A,B)
    return opt[len(arr)-1]

print(dp_opt(arr))
print(dp_opt(arr2))
print(dp_opt(arr3))

