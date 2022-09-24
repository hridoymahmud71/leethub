# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfsTraverse(node,pathVal,targetSum):

            if node == None :
                return False
                  
        
            pathVal.append(node.val)     
            targetSum -= node.val

            if targetSum == 0 and node.left == None and node.right == None:
                result.append(pathVal.copy())

            dfsTraverse(node.left,pathVal,targetSum)
            dfsTraverse(node.right,pathVal,targetSum)

            pathVal.pop()

        
        dfsTraverse(root,[],targetSum)

        return result