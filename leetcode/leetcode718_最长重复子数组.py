class Solution:
    #这个函数是判断两个长度相同的列表最长对应子数组的长度
    #最长对应子数组的长度：列表A和列表B的n个位置，如果某个位置两个列表对应的元素相等
    #那么，这个位置称为“对应”。求连续最长的对应的数量
    #如1234和2345，一个都没有对应
    #如1234和9234，第2、3、4位对应了，那么输出3
    #如12345678和12305608，输出3
    def panduan(self,a,b):
        count = 0
        max_ = 0
        for j in range(len(a)):
            if a[j] == b[j]:
                count += 1
            else:
                if count >= max_:
                    max_ = count
                count = 0
        return max(max_,count)
    def findLength(self, a, b):
        
        c = a.copy()
        d = b.copy()
        e = a.copy()
        f = b.copy()
        
        #慢慢地，各截掉一个元素进行匹配
        max2 = 0
        for i in range(len(e)):
            temp = self.panduan(e,f)
            if temp > max2:
                max2 = temp
            if i >= 1:
                e.pop(0)
                f.pop()
                temp = self.panduan(e,f)
                if temp > max2:
                    max2 = temp
        
        #也是一样，不过方向相反            
        max3 = 0
        for i in range(len(c)):
            temp = self.panduan(c,d)
            if temp > max3:
                max3 = temp
            if i >= 1:
                d.pop(0)
                c.pop() 
                temp = self.panduan(c,d)
                if temp > max3:
                    max3 = temp                    
                    
        return max(max2,max3)
    
    #官方的动态规划方法
    def dp(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)
    
A = [0,0,0,0,1]
B = [1,0,0,0,0]
s = Solution()
print(s.findLength(A,B))
print(s.dp(A,B))