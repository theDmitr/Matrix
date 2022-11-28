from random import randint

class Matrix:
    matrix = []
    def __init__(self, rows, columns):
        self.rows, self.columns = rows, columns
        self.fillCellsByZero()
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
    def addTriangle(self):
        for i in range(self.rows): 
            for j in range(self.columns - 1, self.columns - i, -1): self.matrix[i - 1][j - 1] = 0
    def fillCellsByZeroesAndOnes(self):
        self.fillCellsByZero()
        for i in range(self.rows):
            for j in range(i + 1): self.matrix[i][j] = 1
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
            
    def display(self):
        for i in self.matrix: print(i)