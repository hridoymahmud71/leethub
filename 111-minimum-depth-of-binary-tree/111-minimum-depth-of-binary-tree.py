# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        mindepth = 0
        myqueue = deque()
        myqueue.append(root)
        
        while myqueue :
            currentLevelSize = len(myqueue) 
            mindepth += 1

            for i in range(currentLevelSize):
                current =  myqueue.popleft()

                if current.left == None and current.right == None :
                    return mindepth
                
                if current.left:
                    myqueue.append(current.left)
                if current.right:
                    myqueue.append(current.right)
        
        return mindepth