class Solution:
    #一个格子的前后左右有重复的
    def zhouwei(self,i,j,grid,c):
        temp = 0
        if i+1 < len(grid[0]):
            temp += min(grid[i][j],grid[i+1][j])
        if i-1 > -1:
            temp += min(grid[i][j],grid[i-1][j])
        if j+1 < len(grid[0]):
            temp += min(grid[i][j],grid[i][j+1])
        if j-1 > -1:
            temp += min(grid[i][j],grid[i][j-1])
        c[i][j] = temp
    def surfaceArea(self,grid):       
        c = [[0 for i in range(len(grid[0]))] for j in range(len(grid[0]))]
        count1 = 0
        count2 = 0
        count3 = 0
        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                self.zhouwei(i,j,grid,c)
                count1 += grid[i][j]
                count2 += c[i][j]
                #一个格子上的堆，各个箱子的上面和下面也有重复的
                count3 += max(0,grid[i][j]-1)
        return count1*6 - count2 -count3*2
    
s = Solution()
print(s.surfaceArea([[1,0],[0,2]]))