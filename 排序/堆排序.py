#堆排序(基于小根堆)

#这个函数用于对单个元素进行调整：
#如果这个元素比它的子节点大，那么就把这个元素下沉（调整它和子节点的位置）
#下沉一次后，如果仍然比新的子节点大，那么就继续下沉
#直到下沉到比子节点小或者没有子节点为止
def single(node):
    #这个if表示只有左孩子的情况
    if 2*node == len(lst)-1:
        if lst[node] > lst[2*node]:
            lst[node],lst[2*node] = lst[2*node],lst[node]
    #这个if表示有左右孩子的情况
    elif 2*node < len(lst)-1:
        min_ = min(lst[node],lst[2*node],lst[2*node+1])
        if lst[2*node] == min_:
            lst[node],lst[2*node] = lst[2*node],lst[node]
            single(2*node)
        elif lst[2*node+1] == min_:
            lst[node],lst[2*node+1] = lst[2*node+1],lst[node]
            single(2*node+1)
    #由于lst是可变类型，因此这里不return也可以
    return lst

#建立堆
def struct(lst):
    #最后的非叶子节点的索引是(len(lst)-1)//2
    for i in range((len(lst)-1)//2):
        single((len(lst)-1)//2-i)
    return lst

#主函数
def main(lst):
    #在列表开头增加0元素，这是占位用的
    lst.insert(0,0)
    #ordered是排序后的列表
    ordered = []
    #建立堆
    lst = struct(lst)
    #一步一步抽出最小值，并且调整堆
    for j in range(len(lst)-1):
        #弹出最小的元素
        ordered.append(lst.pop(1))
        #把堆最底端的值放到根部
        lst.insert(1,lst.pop())
        #调整堆
        single(1)
    return ordered


lst = [15,322,16,21,45,17,2,6,12,4,165,47,3,7,122,445,27,115,74,411]
print(lst)
print(main(lst))
    
    
