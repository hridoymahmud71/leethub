# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def dfsTraverse(node,pathVal):
            nonlocal sum

            if node == None :
                return False
                  
            # print(node.val)
            pathVal.append(node.val)     
            

            if node.left == None and node.right == None:
                number = ''.join(map(str,pathVal))
                sum += int(number)

            # print(node.val,pathVal)    
            dfsTraverse(node.left,pathVal)
            dfsTraverse(node.right,pathVal)

            
            pathVal.pop()

        
        dfsTraverse(root,[])

        return sum