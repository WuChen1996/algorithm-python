class Solution:
    #我的超出时间限制的方法
    def canFinish2(self, n, pre) -> bool:
        nan = []
        for i in pre:
            nan.append(i[0])
        yi = [x for x in range(n) if x not in nan]
#        print(yi)
        
        #坑爹的题目描述，原来每个列表只有两个元素，我得转换下
        pre2 = {}
        for lst in pre:
            if lst[0] not in pre2.keys():
                pre2[lst[0]]=lst
            else:
                pre2[lst[0]].extend(lst[1:])
#        print(pre2)
        pre = list(pre2.values())
#        print(pre3)
        
        #循环遍历，直到满足条件为止
        for i in range(n):
            if len(yi) == n:
                return True
            for lst in pre:
                if lst[0] in yi:
                    continue
                for i in range(len(lst)-1,0,-1):
                    if lst[i] not in yi:
                        break
                else:
                    yi.append(lst[0])
#            print(yi)
        if len(yi) == n:
            return True
        else:
            return False
    
    #一个官方解答
    def canFinish(self, numCourses, prerequisites) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
#        print(indegrees)
#        print(adjacency)
        queue = []
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            print(cur, pre)
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        print(indegrees)
        print(adjacency)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: 
                queue.append(i)
        print(queue)
        
        # BFS TopSort.
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: 
                    queue.append(cur)
        return not numCourses


        
s = Solution()
print(s.canFinish(5,[[1,0],[1,2],[0,1],[3,4]]))

        

