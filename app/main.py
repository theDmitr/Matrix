from matrix import Matrix, Operations
matrix_1 = Matrix(3, 3)
matrix_1.fillCellsByList([[1, 2, 3], 
                          [4, 5, 6], 
                          [7, 8, 9]
                        ])
matrix_2 = Matrix(3, 3)
matrix_2.fillCellsByList([[3, 2, 1], 
                          [6, 5, 4], 
                          [9, 8, 7]
                        ])
matrix_1.display()
matrix_2.display()

Operations.multiOfTwoMatrices(matrix_1, matrix_2).display()