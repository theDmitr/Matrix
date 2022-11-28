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
    
    # Fills the matrix with natural numbers with a ladder.
    def fillCellsByNaturalNumbersWithLadder(self):
        for i in range(self.rows):
            for j in range(self.columns): self.matrix[i][j] = j + i + 1
    
    # Matrix display
    def display(self):
        for i in self.matrix: print(i)