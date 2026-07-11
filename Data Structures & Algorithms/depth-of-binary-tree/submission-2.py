
            
            # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # level=0
        
        # if not root:
        #     return 0

        # q= deque()
        # q.append(root)
        # while q:
        #     for _ in range(len(q)):
        #         cur=q.popleft()
        #         if cur.left:
        #             q.append(cur.left)
        #         if cur.right:
        #             q.append(cur.right)
        #     level+=1
            
        # return level 

        res=0
        stack=[(root,1)]

        while stack:
            node, depth=stack.pop()

            if node:
                res=max(res,depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
            
        return res
            