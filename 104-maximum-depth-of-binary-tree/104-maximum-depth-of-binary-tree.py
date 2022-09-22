# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode],level = 0) -> int:
        if root == None :
            return level
        level += 1
        
        return max(self.maxDepth(root.left,level),self.maxDepth(root.right,level))