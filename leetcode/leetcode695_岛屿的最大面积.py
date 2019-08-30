class Solution:
    #长达两小时的失败尝试，通过了706/722个测试用例，尽力了
    def maxAreaOfIsland(self, grid):
        import copy
        grid2 = copy.deepcopy(grid)
        count = 2
        for i in range(len(grid)):
            if i == 0:
                for j in range(len(grid[0])):
                    if j == 0 and grid[0][j] == 1:           
                        grid2[0][j] = count
                        count += 1
                    if j >= 1 and grid[0][j] == 1 and grid[0][j-1] == 0:
#                        print('hh',i,j,count,grid2[0][j-1])
                        grid2[0][j] = count
                        count += 1
                    if j >= 1 and grid[0][j] == 1 and grid[0][j-1] > 0:
#                        print(i,j,count,grid2[0][j-1])
                        grid2[0][j] = grid2[0][j-1]
#                    print(grid2)
            else:
                if i >= 1:
                    for k in range(len(grid[0])-1,0,-1):
                        if grid2[i-1][k] != grid2[i-1][k-1] and grid[i-1][k-1] > 0 and grid2[i-1][k]>0:
                            grid2[i-1][k-1] = grid2[i-1][k]
                    for k in range(len(grid[0])):
                        if k == 0 and grid2[i-1][k] == 1:
                            grid2[i-1][k] = count
                            count += 1
                        if k >= 1 and grid2[i-1][k] == 1 and grid2[i-1][k-1] == 0:
                            grid2[i-1][k] = count
                            count += 1
                        if k >= 1 and grid2[i-1][k] == 1 and grid2[i-1][k-1] > 0:
                            grid2[i-1][k] = grid2[i-1][k-1]      
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        continue
                    else:
                        if grid[i-1][j] == 1:
#                            print(i,j)
                            grid2[i][j] = grid2[i-1][j]
                        elif j-1 >= 0 and grid2[i][j-1] > 1:
                            grid2[i][j] = max(grid2[i-1][j],grid2[i][j-1])  
                            
        i = len(grid)                
        for k in range(len(grid[0])-1,0,-1):
            if grid2[i-1][k] != grid2[i-1][k-1] and grid[i-1][k-1] > 0 and grid2[i-1][k]>0:
                grid2[i-1][k-1] = grid2[i-1][k]
        for k in range(len(grid[0])):
            if k == 0 and grid2[i-1][k] == 1:
                grid2[i-1][k] = count
                count += 1
            if k >= 1 and grid2[i-1][k] == 1 and grid2[i-1][k-1] == 0:
                grid2[i-1][k] = count
                count += 1
            if k >= 1 and grid2[i-1][k] == 1 and grid2[i-1][k-1] > 0:
                grid2[i-1][k] = grid2[i-1][k-1]
                

        for j in range(len(grid[0])-1,-1,-1):
            for i in range(len(grid)-1,0,-1):
                if grid2[i][j]>1 and grid2[i-1][j]>1 and grid2[i][j]>1!=grid2[i-1][j]:
                    grid2[i-1][j] = grid2[i][j]
       
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1):
                if grid2[i][j]>1 and grid2[i][j+1]>1 and grid2[i][j]>1!=grid2[i][j+1]:
                    if i<len(grid)-1:
                        if grid2[i+1][j]>1:
                            grid2[i][j] = grid2[i+1][j]
                            grid2[i][j+1] = grid2[i+1][j]
                        if grid2[i+1][j+1]>1:
                            grid2[i][j] = grid2[i+1][j+1]
                            grid2[i][j+1] = grid2[i+1][j+1]
        M = [j for i in grid2 for j in i]
        L = [x for x in M if x != 0]
        x=dict((a,L.count(a)) for a in L)
        y=[v for k,v in x.items() if max(x.values())==v]
        if y:
            z=y[0]
        else:
            z=0
        return z
    
    #方法二也是一种dps
    def maxAreaOfIsland2(self, grid):
      def f(i,j):
          if i!=0:
              if grid[i-1][j]==1:
                  grid[i-1][j]=-1
                  res.append(1)
                  f(i-1,j)
          if i!=len(grid)-1:
              if grid[i+1][j]==1:
                  grid[i+1][j]=-1
                  res.append(1)
                  f(i+1,j)
          if j!=0:
              if grid[i][j-1]==1:
                  grid[i][j-1]=-1
                  res.append(1)
                  f(i,j-1)
          if j!=len(grid[0])-1:
              if grid[i][j+1]==1:
                  grid[i][j+1]=-1
                  res.append(1)
                  f(i,j+1)
    
      res_max=0
      for i in range(len(grid)):
          for j in range(len(grid[0])):
              if grid[i][j] in (0,-1):
                  continue
              else:
                  res=[1]
                  grid[i][j]=-1
                  f(i,j)
                  print(res)
                  if len(res)>res_max:
                      res_max=len(res)
    
      return res_max



    #方法三：dps
    #遍历二维数组，当值为1时开始dfs，搜索的时候有上下左右四个方向，
    #每当走过一个相邻的1（岛屿）就标记一下（改成-1），这样下次就不会走之前走过的岛屿了
    
    nextStep = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    step = 0
    def maxAreaOfIsland3(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.step = 0
                    self.dfs(grid, i, j)
                    #用于理解代码逻辑
                    print(i,j,res,self.step)
                    res = max(res, self.step)
        return res
    def dfs(self, grid, x, y):
        """
        :type grid: List[list[int]]
        :type x: int
        :type y: int
        :rtype : None
        """
        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] != 1:
            return
        grid[x][y] = -1
        self.step += 1
        for k in range(len(self.nextStep)):
            self.dfs(grid, x + self.nextStep[k][0], y + self.nextStep[k][1])

grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
s = Solution()
print(s.maxAreaOfIsland2(grid))
