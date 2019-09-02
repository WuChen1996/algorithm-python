class Solution:
    def compute(self,n):
        tmp = 0
        for i in range(len(str(n))):
            tmp += int(str(n)[i]) ** 2
        return tmp
    
    #这种compute方法貌似更高级？
    def compute2(self,n):
        #下面的是生成器
        return sum(int(i) ** 2 for i in str(n))
        #正常方法
        return sum([int(i) ** 2 for i in str(n)])
    
    def isHappy(self, n):
        lst = []
        result = n
        while True:
            result = self.compute(result)
            if result == 1:
                return True
            else:
                if result not in lst:
                    lst.append(result)
                else:
                    return False
                
    def isHappy2(self, n: int) -> bool:
        n = str(n)
        slow = n
        fast = str(sum(int(i) ** 2 for i in n))
        print(slow)
        print(fast)
        count = 0
        while slow != fast:
            slow = str(sum(int(i) ** 2 for i in slow))
            fast = str(sum(int(i) ** 2 for i in fast))
            fast = str(sum(int(i) ** 2 for i in fast))
            print(count,'i',slow)
            print(count,'i',fast)
            count+=1
        return slow == "1"

s = Solution()
print(s.isHappy2(19))
#print(s.isHappy2(2))