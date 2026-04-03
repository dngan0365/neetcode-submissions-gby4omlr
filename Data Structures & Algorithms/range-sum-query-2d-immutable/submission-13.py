class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.sumMatrix = [[0]*(self.m+1) for _ in range(self.n)]
        for i in range(self.n):
            curr = 0
            for j in range(1, self.m+1):
                curr += matrix[i][j-1]
                self.sumMatrix[i][j] = curr
        print("prefixSum")
        print(self.sumMatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        print("Sum Region")
        for i in range(row1, row2+1):
            print(self.sumMatrix[i][col2+1] - self.sumMatrix[i][col1])
            total += self.sumMatrix[i][col2+1] - self.sumMatrix[i][col1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)