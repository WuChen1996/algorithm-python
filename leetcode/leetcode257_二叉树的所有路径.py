# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                #这里有一个问题，在输出结果的倒数第二行，path是1->3
                #然而之前path是1->2->5，这是咋回事？
                path += str(root.val)
                print('path',path)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                    print('paths',paths)
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    print('path-after',path)
                    construct_paths(root.left, path)
                    print('yyy')
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths
            
    def binaryTreePaths2(self, root: TreeNode):
        if not root:
            return []
        if not root.left and not root.right:
            print('uuuu',str(root.val))
            return [str(root.val)]
        paths = []
        if root.left:
            for i in self.binaryTreePaths2(root.left):
                print(self.binaryTreePaths2(root.left),i)
                paths.append(str(root.val) + '->' + i)
        if root.right:
            for i in self.binaryTreePaths2(root.right):
                paths.append(str(root.val) + '->' + i)
        return paths  

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
s = Solution()
s.binaryTreePaths(root)