class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

#         numRows = len(mat)
#         numcols = len(mat[0])

#         dp  = [[math.inf for x in range(numcols)] for y in range(numRows)] # fill 2d array with infinity

#         for r in range(numRows):
#             for c in range(numcols):
#                 if mat[r][c] == 0:
#                     dp[r][c] = 0
#                 else:
#                     if r > 0 :
#                         dp[r][c] = min(dp[r][c],dp[r - 1][c] + 1)
#                     if c > 0 :
#                         dp[r][c] = min(dp[r][c],dp[r][c - 1] + 1)

#         for r in range(numRows - 1,-1,-1):
#             for c in range(numcols - 1,-1,-1):
            
#                 if r < numRows - 1 :
#                     dp[r][c] = min(dp[r][c],dp[r + 1][c] + 1)
#                 if c < numcols - 1 :
#                     dp[r][c] = min(dp[r][c],dp[r][c + 1] + 1)


#         return dp
    
        visited = set()
        from collections import deque
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        
        while q:
            x,y = q.popleft()
            for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
                newX, newY = x+dirr[0], y+dirr[1]
                if newX >= 0 and newX <= len(mat)-1 and newY >= 0 and newY <= len(mat[0])-1 and (newX, newY) not in visited:
                        mat[newX][newY] = mat[x][y] + 1
                        visited.add((newX, newY))
                        q.append((newX, newY))
        return mat
    
        