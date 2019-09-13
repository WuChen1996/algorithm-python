import math
class Solution:
    def sqr(self,n):
        a = int(math.sqrt(n))
        return a * a == n
    #我的方法，超出时间限制，用的是动态规划
    def numSquares(self, n: int) -> int:
        if n == 1:return 1
        elif n == 2:return 2
        elif n == 3:return 3
        elif n ==4:return 1
        elif n ==5:return 2
        else:
            lst = [0]*(n+1)
            lst[1] = 1
            lst[2] = 2
            lst[3] = 3
            lst[4] = 1
            lst[5] = 2
            for i in range(6,n+1):
                if self.sqr(i) == True:
                    lst[i] = 1
                    continue
                min_ = n
                for k in range(1,i):
                    if lst[k]+lst[i-k] < min_:
                        min_ = lst[k]+lst[i-k]
                lst[i] = min_
            return lst[n]
        
        
    #改进后的动态规划，通过了，但是时间还是很久
    def numSquares2(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        elif n ==4:
            return 1
        else:
            lst = [0]*(n+1)
            lst[1] = 1
            lst[2] = 2
            lst[3] = 3
            lst[4] = 1
            lst[5] = 2
            for i in range(6,n+1):
                min_ = n
                #我也不知道阐释改进的地方在哪，去看leetcode官方图解
                for t in range(1,int(i**0.5)+1):                   
                    if i-t*t >= 0:
                        if lst[i-t*t]+1 < min_:
                            min_ =  lst[i-t*t]+1
                    else: 
                        break
                    
                lst[i] = min_
                
            print(lst)
            return lst[n]
s = Solution()
print(s.numSquares2(123))



