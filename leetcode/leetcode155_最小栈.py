#我的最自然的最简单的解法
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        del(self.stack)[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_ = self.stack[0]
        for i in self.stack:
            if i < min_:
                min_ = i
        return min_

class MinStack2:
    # 辅助栈和数据栈同步
    # 思路简单不容易出错

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]


obj = MinStack2()
obj.push(-3)
obj.push(43)
obj.push(5)
obj.getMin()
obj.push(83)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()