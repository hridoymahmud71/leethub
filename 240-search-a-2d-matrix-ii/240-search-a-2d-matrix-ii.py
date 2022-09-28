class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        def divideAndConquer(r, c):

            current = matrix[r][c]

            if current == None:
                return False
            if current == target:
                return True

            matrix[r][c] = None

            if current > target:
                return (r > 0 and divideAndConquer(r - 1, c)) or (c > 0 and divideAndConquer(r, c - 1))
            else:
                return (r < rows and divideAndConquer(r + 1, c)) or (c < cols and divideAndConquer(r, c + 1))

        return divideAndConquer(0, 0)