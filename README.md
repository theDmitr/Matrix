# Matrix

This library will help you work with matrices, fill them in and perform operations on them.

## Tutorial

To work with the matrix, you need to import the module, this can be done using:

```sh
from matrix import Matrix
```

To create a matrix object, you need to initialize it, call the constructor from the "Matrix" class.
The constructor method takes 2 required arguments — the number of rows and columns of the created matrix.

```sh
matrix = Matrix(rows, columns)
```

### Methods of the Matrix class

| Method | Assignment | Use |
| - | - | - |
| fillCellsByZero | Fills all matrix cells with zeros. | matrix.fillZeroesAndOnes() |
| fillCellsByRandomNumbers | Fills matrix cells with random numbers from a range. It takes one argument as input - a range (tuple).  | matrix.fillZeroesAndOnes((a, b)) |
| addTriangle | Adds a triangle of zeros to the center of the matrix. | matrix.addTriangle() |
| fillCellsByZeroesAndOnes | Fills everything above the main diagonal with zeros, the rest with ones. | matrix.fillCellsByZeroesAndOnes() |
| fillCellsByNaturalNumbersWithLadder | Fills the matrix with natural numbers with a ladder. | matrix.fillCellsByNaturalNumbersWithLadder() |
| display | Matrix display. | matrix.display() |