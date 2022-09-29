# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        globalMin = float(inf)
        
        def DFS(node,visited):
            if node == None :return 
            nonlocal globalMin
            
            for i in range(len(visited)):                
                globalMin = min(abs(node.val - visited[i]),globalMin)
            
            visited.append(node.val)
        
            DFS(node.left,visited)
            DFS(node.right,visited)
            
            visited.pop()
            
        DFS(root,[])
        
        return globalMin
        