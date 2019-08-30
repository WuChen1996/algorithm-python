class Solution:
    #超时
    def countPrimes(self, n: int):
        if n <= 2:
            return 0
        else:
            lst = list(range(2,n))
            lst3=[]
            while True:
                if len(lst)>1:
                    if lst[0] < n**0.5:
                        lst = [x for x in lst if x%lst[0] != 0]
                        lst3.append(lst[0])
                    else:
                        lst3 = lst3 + lst[1:]
                        break
                else:
                    break
            return len(lst3)+1
        

    def countPrimes2(self, n: int):
        if n <= 2:
            return 0 
        else:
            lst = [1]*n
            lst[0],lst[1] = 0,0
            for i in range(2,int(n**0.5)+1):
                if lst[i] == 1:
                    for j in range(i*i,n,i):
                        lst[j] = 0
            return sum(lst)
            

    def countPrimes3(self, n: int):
            if n < 3:
                return 0     
            else:
                # 首先生成了一个全部为1的列表
                output = [1] * n
                # 因为0和1不是质数,所以列表的前两个位置赋值为0
                output[0],output[1] = 0,0
                 # 此时从index = 2开始遍历,output[2]==1,
                 # 表明第一个质数为2,然后将2的倍数对应的索引
                 # 全部赋值为0. 此时output[3] == 1,即表明下一个质数为3,
                 # 同样划去3的倍数.以此类推.
                for i in range(2,int(n**0.5)+1): 
                    if output[i] == 1:
                        output[i*i:n:i] = [0] * len(output[i*i:n:i])
             # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
            print(output)
            return sum(output)
        
s = Solution()
print(s.countPrimes2(10))