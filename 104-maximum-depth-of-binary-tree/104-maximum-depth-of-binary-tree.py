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


        def dfsTrasverse(current,level):
            if current == None :
                return level
            level += 1
            
            return max(dfsTrasverse(current.left,level),dfsTrasverse(current.right,level)) 
            

        
        return dfsTrasverse(root,0)