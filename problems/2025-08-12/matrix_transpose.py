# Problem Name: Matrix Transpose
# Description:
#   Write a function transpose(matrix) that returns the transpose of a matrix.
#   In the main part, take the matrix dimensions and elements, call transpose, and print the transposed matrix.
#
# Input Format:
#   First line: two integers r c
#   Next r lines: each line has c integers (matrix rows)


def transpose(matrix):
    r = len(matrix)
    c = len(matrix[0])
    transpose_matrix = [[0 for _ in range(r)] for _ in range(c)]
    
    for i in range(r):
        for j in range(c):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix


try:
    r, c = map(int, input().split())
    
    matrix = []
    for _ in range(r):
        value = list(map(int,input().split()))
        matrix.append(value)
    
    result_matrix = transpose(matrix)
    
    for value in result_matrix:
        print(*value)
        
except ValueError:
    print("Please enter valid integers.")