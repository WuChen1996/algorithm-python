# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        def cur(root):
            if not root:
                return 0
            left_depth = cur(root.left)
            if left_depth==-1:
                return -1
            right_depth = cur(root.right)
            if right_depth==-1:
                return -1
            if abs(left_depth - right_depth)<=1:
                return max(left_depth,right_depth)+1
            else:
                return -1
        return cur(root)>0
    def isBalanced2(self, root) -> bool:
        def cal_depth(root):
            if not root:
                return 0
            left = cal_depth(root.left)
            right = cal_depth(root.right)
            return max(left, right) + 1
        def cur(root):
            if not root:
                return True
            if abs(cal_depth(root.left)-cal_depth(root.right))>1:
                return False
            if not cur(root.left):
                return False
            if not cur(root.right):
                return False
            else:
                return True
        return cur(root)

            
    
root = TreeNode(1) 
root.left= TreeNode(2) 
root.right= TreeNode(3)
root.right.left= TreeNode(4) 

s = Solution()
print(s.isBalanced2(root))
