
class Solution:
    def isValid(self, a: str) -> bool:
        if a == '':
            return True
        dic = {'[':']','(':')','{':'}'}
        if a[0] == ']' or a[0]=='}' or a[0]==')':
            return False
        stack = []
        for char in a:
            if char in dic:
                stack.append(char)
            else:
                if stack:
                    if char != dic[stack.pop()]:
                        return False
                else:
                    return False
        else:
            return not stack