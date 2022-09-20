class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        numRows = len(mat)
        numcols = len(mat[0])

        dp  = [[math.inf for x in range(numcols)] for y in range(numRows)] # fill 2d array with infinity

        for r in range(numRows):
            for c in range(numcols):
                if mat[r][c] == 0:
                    dp[r][c] = 0
                else:
                    if r > 0 :
                        dp[r][c] = min(dp[r][c],dp[r - 1][c] + 1)
                    if c > 0 :
                        dp[r][c] = min(dp[r][c],dp[r][c - 1] + 1)

        for r in range(numRows - 1,-1,-1):
            for c in range(numcols - 1,-1,-1):
            
                if r < numRows - 1 :
                    dp[r][c] = min(dp[r][c],dp[r + 1][c] + 1)
                if c < numcols - 1 :
                    dp[r][c] = min(dp[r][c],dp[r][c + 1] + 1)


        return dp