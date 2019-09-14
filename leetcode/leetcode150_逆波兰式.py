class Solution:
    def evalRPN(self,lst) -> int:
        fuhao = ['+','-','*','/']
        stack = []
        while lst:
            if lst[0] not in fuhao:
                stack.append(lst.pop(0))
            else:
                x = 'int('+ stack.pop(-2)+lst.pop(0)+stack.pop() +')'
                a = eval(x)
                stack.append(str(a))
        return stack[0]

        
s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))