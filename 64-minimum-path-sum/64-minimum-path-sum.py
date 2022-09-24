class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # -----start-----
        # recursive way with memo

        m = len(grid) - 1
        n = len(grid[0]) - 1
        memo = {}

        def dfsTraverse(m, n, memo):

            memkey = str(m)+"-"+str(n)

            if memkey in memo.keys():
                return memo[memkey]

            if m == 0 and n == 0:
                return grid[m][n]

            if m < 0 or n < 0:
                return float('inf')

            memo[memkey] = min(dfsTraverse(m-1, n, memo),
                               dfsTraverse(m, n-1, memo)) + grid[m][n]
            return memo[memkey]

        return  dfsTraverse(m, n, memo)