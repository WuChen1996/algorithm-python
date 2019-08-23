#假设没有0出现
a = 34547
a = str(a)
g = [0]*(len(a)+1)
print(g)
g[0] = 1
g[1] = int(a[0])
g[2] = max(int(a[0])+int(a[1]),int(a[0]+a[1]))

for i in range(3,len(a)+1):
    head = ''
    for z in range(i):
        head = head + a[z]
    max_ = 0
    
    for j in range(1,i+1):
        tail = ''
        for k in range(j):
            tail = str(head[-k-1]) + tail
            if i == 3:
                print(j,k,tail)
        if int(g[i-j])*int(tail) > max_:
            max_ = int(g[i-j])*int(tail)
    g[i] = max_
print(g)