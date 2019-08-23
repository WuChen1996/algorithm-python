lst= [4,3,2,1]

def next_(lst):
    count = 0
    for i in range(1,len(lst)):
        print('f')
        if lst[len(lst)-i] > lst[len(lst)-i-1]:
            count += 1
            break
    print(len(lst)-i)
    print(i)
    print('count',count)
    if count == 0:
        return lst.reverse()
    else:
        tail=lst[len(lst)-i:]
        print(tail)
        print(min(tail))
        index_ = len(lst)-i+tail.index(min(tail))
        if min(tail)>lst[len(lst)-i-1]:
            print('ffff')
            lst[len(lst)-i-1],lst[index_] = lst[index_],lst[len(lst)-i-1]
            tail2 = lst[len(lst)-i:]
            print(tail2)
            tail2.sort()
            print(tail2)
            lst[len(lst)-i:] = tail2
        else:
            tail3 = lst[len(lst)-i:]
            min_ = tail3[0]
            for k in range(len(tail3)):
                if tail3[k]>lst[len(lst)-i-1] and tail3[k]<min_:
                    min_ = tail3[k]
            print(tail3)
            print(min_)
            index2_ = len(lst)-i+tail3.index(min_)
            print(index2_)
            lst[len(lst)-i-1],lst[index2_] = lst[index2_],lst[len(lst)-i-1]
            tail4 = lst[len(lst)-i:]
            tail4.sort()
            print(tail4)
            lst[len(lst)-i:] = tail4
            pass
next_(lst)       
print(lst)