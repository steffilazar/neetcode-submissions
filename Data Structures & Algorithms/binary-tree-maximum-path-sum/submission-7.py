# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path=0
        res=float('-inf')
        def getmax(root):
            nonlocal res
            if not root:
                return 0
            
            left=getmax(root.left)
            right=getmax(root.right)
            self.path = max(0,root.val + max(left, right))
            res=max(res, root.val+left+right)
            return self.path


        getmax(root)
        return res
        

        