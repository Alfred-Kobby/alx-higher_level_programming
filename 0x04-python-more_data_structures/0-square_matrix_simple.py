#!/usr/bin/python3
"""
Compute the square value of all integers of a matrix
"""
def square_matrix_simple(matrix=[]):
    return ([[(x**2) for x in row] for row in matrix])
