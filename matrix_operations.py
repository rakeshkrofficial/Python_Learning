"""Develop a Python program with user-defined functions for matrix  addition, subtraction, and multiplication. Allow the user to input two  matrices and choose the operation.   """

def add_matrix(matrix_1,matrix_2):

    result = []

    for i in len(matrix_1):
        row = []

        for j in range(len(matrix_2)):

            row.append(matrix_1[i][j] + matrix_2[i][j])

        result.append(row)

    return result

def substract_matrix(matrix_1,matrix_2):

    result = []

    for i in range(len(matrix_1)):

        row = []

        for j in len(matrix_2):

            row.append(matrix_1[i][j] - matrix_2[i][j])

        result.append(row)

    return result

def multiply_matrix(matrix_1,matrix_2):

    result = []

    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                result[i][j] += matrix_1[i][k]*matrix_2[k][j]
