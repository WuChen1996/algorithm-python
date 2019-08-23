input_="134345762125579"
lst = [int(x) for x in input_]
#lst=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

clst = [1]*len(lst)#这个列表存储当前最大值
print('原列表：',lst)

for i in range(1,len(lst)):
    max_ = 1
    for j in range(i):     
        if lst[j] < lst[i]:
            if clst[j] > max_:
                max_ = clst[j]
    clst[i] = max_ + 1 if lst[i] != 1 else 1
print('顺序值：',clst)