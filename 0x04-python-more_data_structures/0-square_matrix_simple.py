#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for i in range(3):
        m.append([])
        for j in range(len(matrix[i])):
            m[i].append(matrix[i][j] ** 2)
    return m
