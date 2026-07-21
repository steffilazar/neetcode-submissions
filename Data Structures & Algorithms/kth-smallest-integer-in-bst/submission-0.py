# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.res=[]
        
        def inorder(node):
            if not node:
                return None

            inorder(node.left)
            self.res.append(node.val)
            inorder(node.right)
        inorder(root)
        i=-1
        for _ in range(k):
            i+=1
        return self.res[i]



