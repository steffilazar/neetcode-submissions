# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
    

        stack=[(root, root.val)]
        while stack:
                node, maxval=stack.pop()
            
                
                if node.val>=maxval:
                    res+=1

                newpathmax=max(maxval,node.val)
                
                if node.left:
                    stack.append((node.left,newpathmax))
                if node.right:
                    stack.append((node.right,newpathmax))

            
        return res