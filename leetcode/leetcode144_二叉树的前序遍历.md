迭代
```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = deque([root])
        output = []
        while stack:
            tmp = stack.pop()
            output.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return output
```


递归
```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # print(root.val)
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        else:
            return [root.val] +self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def r(root):
            # print(root.val,re)
            if not root:
                return 
            # if not root.left and not root.right:
            #     re.append(root.val)
            #     # print(123,root.val,re)
            #     return
            # else:
            re.append(root.val)
            r(root.left)
            r(root.right)
            
        re = []
        r(root)
        return re
```
