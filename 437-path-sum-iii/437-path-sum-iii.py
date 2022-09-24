# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0

        def dfsTraverse(node,pathVal,targetSum):

            if node == None :
                return False
                  
        
            pathVal.append(node.val)     
            
            localSum = 0
            nonlocal result
            for i in range(len(pathVal) -1,-1,-1):
                localSum += pathVal[i]
                if localSum == targetSum:
                    result += 1

            dfsTraverse(node.left,pathVal,targetSum)
            dfsTraverse(node.right,pathVal,targetSum)

            pathVal.pop()

        
        dfsTraverse(root,[],targetSum)

        return result