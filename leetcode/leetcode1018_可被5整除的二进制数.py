class Solution:
    #这个方法好，用时超过了75%，内存超过了100%
    def prefixesDivBy5(self, a):
        b = [0]*(len(a))
        if a[0]== 0:
            b[0] = True 
            tt = 0
        else:
            b[0] = False
            tt = 1
        for i in range(1,len(a)):
            if b[i-1] == True:
                if a[i] == 0 : 
                    b[i] = True
                    tt = 2*tt
                else : 
                    b[i] = False
                    tt = 2*tt +1
            else:
                if a[i] == 0 : 
                    b[i] = False
                    tt = 2*tt
                else:
                    tt = 2*tt+1
                    b[i] = True if tt % 5 == 0 else False
        return(b)
        
    def prefixesDivBy5_2(self, a):
        b = [0]*(len(a))
        tmp = 0
        for i in range(len(a)):
             tmp = 2*tmp+1 if a[i] == 1 else 2*tmp
             b[i] = True if tmp%5 == 0 else False
        return b
s = Solution()
print(s.prefixesDivBy5_2([1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0]))
