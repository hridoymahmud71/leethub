# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        globalMax = 0

        def dfsTrasverse(current,level):
            if current == None :
                return
            level += 1
            nonlocal globalMax
            globalMax = max(level,globalMax)
            dfsTrasverse(current.left,level)
            dfsTrasverse(current.right,level)

        
        dfsTrasverse(root,0)

        
        return globalMax