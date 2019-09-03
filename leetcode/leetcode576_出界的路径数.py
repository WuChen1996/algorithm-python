class Solution:
    #动态规划
    def findPaths(self, m: int, n: int, N: int, ii: int, jj: int) -> int:
        if N == 0:
            return 0
        dp = [[[0 for i in range(n+2)] for j in range(m+2)] for k in range(N+1)]

        #初始化
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i <= 1:
                    dp[1][i][j] += 1
                if i >= m:
                    dp[1][i][j] += 1
                if j <= 1:
                    dp[1][i][j] += 1
                if j >= n:
                    dp[1][i][j] += 1
        
        #开始递推了
        for k in range(2,N+1):
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if i > 1:
                        dp[k][i][j] += dp[k-1][i-1][j]
                    if i <m:
                        dp[k][i][j] += dp[k-1][i+1][j]
                    if j > 1:
                        dp[k][i][j] += dp[k-1][i][j-1]
                    if j < n:
                        dp[k][i][j] += dp[k-1][i][j+1]

        sum = 0
        for i in range(N+1):
            sum += dp[i][ii+1][jj+1]
        mod_ = sum%1000000007
        return mod_
                    
s = Solution()
print(s.findPaths(8,50,23,5,26))
