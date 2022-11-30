# Matrix

This library will help you work with matrices, fill them in and perform operations on them.

## Tutorial

To work with the matrix, you need to import the module, this can be done using:

```python
from matrix import Matrix
```

To create a matrix object, you need to initialize it, call the constructor from the "Matrix" class.
The constructor method takes 2 required arguments — the number of rows and columns of the created matrix.

```python
matrix = Matrix(rows, columns)
```

### Methods of the Matrix class

| Method | Assignment | Use |
| - | - | - |
| fillCellsByList | Fills in a two-dimensional array equivalent to the array passed in the argument. If the dimensions match and the matrix is full, then the method will return True, otherwise False. | matrix.fillCellsByList(array) |
| fillCellsByZero | Fills all matrix cells with zeros. | matrix.fillZeroesAndOnes() |
| fillCellsByRandomNumbers | Fills matrix cells with random numbers from a range. It takes one argument as input - a range (tuple).  | matrix.fillZeroesAndOnes((a, b)) |
| fillCellsByZeroesAndOnes | Fills everything above the main diagonal with zeros, the rest with ones. | matrix.fillCellsByZeroesAndOnes() |
| fillCellsByNaturalNumbersWithLadder | Fills the matrix with natural numbers with a ladder. | matrix.fillCellsByNaturalNumbersWithLadder() |
| fillCellsInSpiral | Fills the matrix with natural numbers in a spiral. | matrix.fillCellsInSpiral() |
| addTriangle | Adds a triangle of zeros to the center of the matrix. | matrix.addTriangle() |
| swapRowsAndColumns | Swaps rows and columns. | matrix.swapRowsAndColumns() |
| getSumAllCells | Returns the sum of all cells in a matrix. | matrix.getSumAllCells() |
| getLowerAndUpperCellsOverMain | Returns a dictionary with elements below and above the main diagonal. | matrix.getLowerAndUpperCellsOverMain() |
| getAverageOverMain | Returns a dictionary with the arithmetic mean of the elements above and below the main diagonal. | matrix.getAverageOverMain() |
| display | Matrix display. | matrix.display() |

## Operations

This class is designed to automate operations on matrices.

```python
from matrix import Operations
```

### Methods of the Operations class
| Method | Assignment | Use |
| - | - | - |
| sumOfTwoMatrices | The simple sum of two matrices. In case of size mismatch, None will be returned. If everything is OK, then the Matrix object is returned. | sumOfTwoMatrices(matrix_1, matrix_2) |
| differenceOfTwoMatrices | The simple difference of two matrices. In case of size mismatch, None will be returned. If everything is OK, then the Matrix object is returned. | differenceOfTwoMatrices(matrix_1, matrix_2) |
| multiOfTwoMatrices | Multiplication of two matrices. If the size does not match, None will be returned, if everything is in order - an object of the Matrix class. | multiOfTwoMatrices(matrix_1, matrix_2) |

## Examples

```python
from matrix import Matrix, Operations
```

### One

```python
matrix = Matrix(7, 7)
matrix.fillCellsByRandomNumbers((1, 9))
matrix.addTriangle()
matrix.display()
```

### Two

```python
N = int(input("Enter N: "))
matrix = Matrix(N, N)
matrix.fillCellsByZeroesAndOnes()
```

### Three

```python
N = int(input("Enter N: "))
M = int(input("Enter M: "))
matrix = Matrix(N, M)
matrix.fillCellsByNaturalNumbersWithLadder()
```

### Four

```python
N = int(input("Enter N: "))
M = int(input("Enter M: "))
matrix = Matrix(N, M)
matrix.fillCellsInSpiral()
```

### Five

```python
matrix = Matrix(7, 3)
matrix.fillCellsByRandomNumbers((1, 9))
matrix.getSumAllCells()
```

### Six

```python
matrix_1 = Matrix(3, 1)
matrix_1.fillCellsByRandomNumbers((1, 9))
matrix_2 = Matrix(1, 3)
matrix_2.fillCellsByRandomNumbers((1, 9))
result_matrix = Operations.multiOfTwoMatrices(matrix_1, matrix_2)
```

### Seven

```python
matrix = Matrix(3, 3)
matrix.fillCellsByRandomNumbers((1, 9))
matrix.getAverageOverMain()
```

### Eight

```python
matrix = Matrix(3, 3)
matrix.swapRowsAndColumns()
```