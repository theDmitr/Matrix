from random import randint
from statistics import mean

class Matrix:
    matrix = []
    def __init__(self, rows, columns):
        self.rows, self.columns = rows, columns
        self.fillCellsByZero()
    def fillCellsByList(self, matrix):
        for i in range(len(matrix)):
            if len(matrix[0]) != len(matrix[i]): return False
        self.matrix = matrix
        return True
    def fillCellsByZero(self):
        self.matrix = []
        for i in range(self.rows):
            line = []
            for j in range(self.columns): line.append(0)
            self.matrix.append(line)
    def fillCellsByRandomNumbers(self, rangeNumbers):
        self.matrix = []
        for i in range(self.rows):
            line = []
            for j in range(self.columns): line.append(randint(rangeNumbers[0], rangeNumbers[1]))
            self.matrix.append(line)
    def fillCellsByZeroesAndOnes(self):
        self.fillCellsByZero()
        for i in range(self.rows):
            for j in range(i + 1, self.columns): self.matrix[i][j] = 1
    def fillCellsByNaturalNumbersWithLadder(self):
        for i in range(self.rows):
            for j in range(self.columns): self.matrix[i][j] = j + i + 1
    def fillCellsInSpiral(self):
        self.fillCellsByZero()
        left, right, down, up = False, True, False, False
        x, y = 0, 0 
        count = 1
        leftLimit, rightLimit, bottomLimit, topLimit = 0, self.columns - 1, self.rows - 1, 1
        while True:
            if count == self.columns * self.rows + 1: break
            self.matrix[y][x] = count
            count += 1
            if right and x == rightLimit:
                rightLimit -= 1
                right, down = False, True
            elif down and y == bottomLimit:
                bottomLimit -= 1
                down, left = False, True
            elif left and x == leftLimit:
                leftLimit += 1
                left, up = False, True
            elif up and y == topLimit:
                topLimit += 1
                up, right = False, True  
            if right: x += 1
            elif left: x -= 1
            elif down: y += 1
            elif up: y -= 1
    def addTriangle(self):
        for i in range(self.rows): 
            for j in range(self.columns - 1, self.columns - i, -1): self.matrix[i - 1][j - 1] = 0
    def swapRowsAndColumns(self):
        newMatrix = [[] for i in range(self.columns)]
        for i in range(self.rows):
            for j in range(self.columns): newMatrix[j].append(self.matrix[i][j])
        self.matrix = newMatrix
    def removeRowAndColumnByMax(self):
    	idx = self.getIndexMaxElement()
    	self.matrix.pop(idx["row"])
    	for i in self.matrix:
    		i.pop(idx["column"])
    def getSumAllCells(self):
        return sum([sum(i) for i in self.matrix])
    def getLowerAndUpperCellsOverMain(self):
        upper, lower = [], []
        for i in range(self.rows):
            for j in range(i + 1, self.columns): upper.append(self.matrix[i][j])
            for k in range(0, i): lower.append(self.matrix[i][k])
        return {"lower": lower, "upper": upper}
    def getAverageOverMain(self):
        cells = self.getLowerAndUpperCellsOverMain()
        return {"lower": mean(cells["lower"]), "upper": mean(cells["upper"])}
    def getMaxElement(self):
    	return max([max(i) for i in self.matrix])
    def getIndexMaxElement(self):
    	maximum = self.getMaxElement()
    	for line, i in enumerate(self.matrix):
    		try:
    			return {"row": line, "column": i.index(maximum)}
    		except: continue
    		
    def display(self):
        for i in self.matrix: print(i)

class Operations:
    def sumOfTwoMatrices(matrix_1, matrix_2):
        if not (matrix_1.rows == matrix_2.rows and matrix_1.columns == matrix_2.columns): return None
        resultMatrix = Matrix(matrix_1.rows, matrix_1.columns)
        for i in range(matrix_1.rows):
            for j in range(matrix_2.columns): 
                resultMatrix.matrix[i][j] = matrix_1.matrix[i][j] + matrix_2.matrix[i][j]
        return resultMatrix
    def differenceOfTwoMatrices(matrix_1, matrix_2):
        if not (matrix_1.rows == matrix_2.rows and matrix_1.columns == matrix_2.columns): return None
        resultMatrix = Matrix(matrix_1.rows, matrix_1.columns)
        for i in range(matrix_1.rows):
            for j in range(matrix_2.columns): 
                resultMatrix.matrix[i][j] = matrix_1.matrix[i][j] - matrix_2.matrix[i][j]
        return resultMatrix
    def multiOfTwoMatrices(matrix_1, matrix_2):
        if not matrix_1.columns == matrix_2.rows: return None
        resultMatrix = Matrix(matrix_1.rows, matrix_2.columns)
        for i in range(matrix_1.rows):
            for j in range(matrix_2.columns):
                resultMatrix.matrix[i][j] = sum([matrix_1.matrix[i][k] * matrix_2.matrix[k][j] for k in range(matrix_2.rows)])
        return resultMatrix